import os
from fastapi import FastAPI
from pydantic import BaseModel
import httpx

MICRO_SERVICE_URL = os.getenv("MICRO_SERVICE_URL") # "http://llm-service-cluste-ip:8000/complete/"


app = FastAPI()

@app.get("/")

def root():
    return "Hello, world!"

async def call_llm_service_get_response(content):
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(MICRO_SERVICE_URL, json = content)
            return response.json()
        except Exception as e:
            return {"result":f"Error returning response from LLM service:{e}"}
    

class rewriteRequest(BaseModel):
    message:str
@app.post("/grammar_check/")
    
async def do_grammar_check(request:rewriteRequest):
    system_prompt = """
    You are an advanced language assistant. Your task is to:
    1.Grammar & Spelling Check: Review the entire input for grammatical correctness, spelling errors, and punctuation issues.
    2.Error Listing: List all identified errors along with their corrected forms.
    3.Partial Input: For incomplete inputs (e.g., single words or phrases), check and correct any spelling or suggest proper alternatives.

    Strict Output Format: Follow the exact format below without leaving anything out or adding anything else. Always check the entire input:

    Corrected Version: 
    [Corrected text]
    Errors Found: [Based on the corrected text, list of errors that is different from the original input]
    
    No Changes: If no corrections or improvements are needed for the entire input, respond exactly with:

    Corrected Version: No corrections needed.
    Errors Found: No errors found.
    
    Important Rules:

    1.Always include all parts of the input in the corrected version, even if there are no changes.
    2.Use the exact phrase "No corrections needed" when applicable—do not change or omit this phrase.
    3.Ensure that both sections (Corrected Version and Errors Found) are always present, even if no changes are made.
    """
    user_prompt = request.message
    
    return await call_llm_service_get_response({"system":system_prompt, "user":user_prompt})
    