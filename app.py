import streamlit as st
import requests
import pandas as pd

# Page Configuration
st.set_page_config(page_title="AI Recruiter Copilot", page_icon="🚀", layout="wide")
st.title("🚀 AI Recruiter Copilot")
st.markdown("Upload resumes, paste your Job Description (JD), and let AI rank candidates.")

API_URL = "http://localhost:8000/api/evaluate"

# Input Section
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Job Description")
    job_desc = st.text_area("Paste the exact Job Description here", height=250)

with col2:
    st.subheader("2. Resumes")
    uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

# Trigger Action
if st.button("Generate Hiring Report", type="primary"):
    if not job_desc or not uploaded_files:
        st.warning("Please provide both a Job Description and at least one Resume.")
    else:
        with st.spinner(f"Analyzing {len(uploaded_files)} candidate(s)... This might take a minute."):
            # Prepare files and data for POST request
            files_payload = [
                ("files", (file.name, file.getvalue(), "application/pdf")) 
                for file in uploaded_files
            ]
            data_payload = {"job_description": job_desc}
            
            try:
                response = requests.post(API_URL, data=data_payload, files=files_payload)
                
                if response.status_code == 200:
                    results = response.json().get("results", [])
                    st.success("Analysis Complete!")
                    
                    # --- DASHBOARD UI ---
                    st.subheader("🏆 Candidate Rankings")
                    
                    # Sort by match_score and display in a clean Pandas DataFrame
                    df = pd.DataFrame(results)
                    if not df.empty and "match_score" in df.columns:
                        df = df.sort_values(by="match_score", ascending=False).reset_index(drop=True)
                        st.dataframe(
                            df[["candidate_name", "match_score", "hiring_recommendation"]], 
                            use_container_width=True
                        )
                    
                    st.divider()
                    st.subheader("📄 Detailed Evaluation Reports")
                    
                    for res in results:
                        name = res.get('candidate_name', 'Unknown')
                        score = res.get('match_score', 0)
                        
                        with st.expander(f"{name} - Match Score: {score}%"):
                            st.markdown(f"**Recommendation:** {res.get('hiring_recommendation', 'N/A')}")
                            
                            c1, c2 = st.columns(2)
                            with c1:
                                st.markdown("### ✅ Strengths")
                                for s in res.get("strengths", []):
                                    st.markdown(f"- {s}")
                            with c2:
                                st.markdown("### 🚩 Weaknesses & Red Flags")
                                for w in res.get("weaknesses", []):
                                    st.markdown(f"- {w}")
                                    
                            st.markdown("### 🎙️ Suggested Interview Questions")
                            for q in res.get("interview_questions", []):
                                st.markdown(f"1. {q}")
                                
                else:
                    st.error(f"Error from Backend: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to the backend API. Is FastAPI running? Error: {e}")