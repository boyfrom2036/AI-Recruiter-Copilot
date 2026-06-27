from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List
import asyncio
from backend.document_processor import extract_text_from_pdf
from backend.vector_stores import ResumeStore
from backend.ai_agent import MistralRecruiter
import dotenv

dotenv.load_dotenv()

app = FastAPI(title="AI Recruiter Copilot API")
store = ResumeStore()

try:
    ai_service = MistralRecruiter()
except ValueError as e:
    ai_service = None
    print(f"Warning: {e}")

# --- ASYNC BATCHING LOGIC ---
# This limits us to 5 concurrent API calls to Mistral at any given time.
# If you have a higher API tier, you can increase this number for faster processing.
MAX_CONCURRENT_REQUESTS = 5
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

async def process_single_resume(file: UploadFile, job_description: str, content: bytes):
    """Worker function that processes a single resume safely under the semaphore limit."""
    async with semaphore:
        # 1. Extract text
        resume_text = extract_text_from_pdf(content)
        
        # 2. Save to Vector DB
        store.add_resume(file.filename, resume_text)
        
        # 3. Evaluate with Mistral AI (This is now awaited)
        eval_result = await ai_service.evaluate_candidate(resume_text, job_description)
        
        # Format edge cases
        if eval_result.get("candidate_name", "Unknown") == "Unknown":
            eval_result["candidate_name"] = file.filename
            
        return eval_result

@app.post("/api/evaluate")
async def evaluate_resumes(
    job_description: str = Form(...),
    files: List[UploadFile] = File(...)
):
    if not ai_service:
        raise HTTPException(status_code=500, detail="Mistral API key not configured")
        
    tasks = []
    
    # Queue up all the files as asynchronous tasks
    for file in files:
        if not file.filename.endswith(".pdf"):
            continue
            
        content = await file.read()
        tasks.append(process_single_resume(file, job_description, content))
        
    # Fire them all off concurrently and wait for them to finish
    results = await asyncio.gather(*tasks)
        
    return {"results": results}