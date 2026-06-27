import os
import json
from mistralai.client import Mistral

class MistralRecruiter:
    def __init__(self):
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError("MISTRAL_API_KEY environment variable is missing.")
        self.client = Mistral(api_key=api_key)
        self.model = "mistral-large-latest"

    # 1. We make this an async function
    async def evaluate_candidate(self, resume_text: str, job_description: str) -> dict:
        prompt = f"""
        You are an expert technical recruiter AI.
        Compare the following resume against the job description.
        
        Job Description:
        {job_description}
        
        Resume:
        {resume_text}
        
        Analyze the candidate and return a strict JSON object with EXACTLY these keys:
        - "candidate_name": string (Extract from resume or use "Unknown")
        - "match_score": integer (0 to 100 representing the fit)
        - "strengths": list of strings (Key matching skills and experience)
        - "weaknesses": list of strings (Missing skills, gaps, or red flags)
        - "interview_questions": list of strings (3 technical/behavioral questions to ask)
        - "hiring_recommendation": string (A 1-2 sentence summary of whether to proceed)
        """
        
        response = await self.client.chat.complete_async(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI that strictly outputs valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        try:
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"JSON Parsing Error: {e}")
            return {}