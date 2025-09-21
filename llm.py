# app/llm.py
import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from app.config import OPENAI_API_KEY

# ---------- Config ----------
router = APIRouter()
if not OPENAI_API_KEY:
    raise RuntimeError("❌ Missing OPENAI_API_KEY. Set it in your .env")

client = OpenAI(api_key=OPENAI_API_KEY)

# ---------- Request Model ----------
class ChatRequest(BaseModel):
    message: str
    use_web: bool = False  # optional, in case you want web scraping later

# ---------- Helper Function ----------
def extract_answer(response):
    """Extract a clean string from LLM response objects."""
    answer_text = ""

    if isinstance(response, list):
        for item in response:
            answer_text += extract_answer(item) + " "
        return answer_text.strip()

    if hasattr(response, "content") and response.content:
        return str(response.content)

    if hasattr(response, "summary") and response.summary:
        return " ".join(response.summary)

    if hasattr(response, "arguments") and response.arguments:
        result = response.arguments.get("result")
        if result:
            return str(result)
        return str(response.arguments)

    return "Sorry, I could not generate an answer."

# ---------- Chat Endpoint ----------
@router.post("/chat/")
async def chat_endpoint(request: ChatRequest):
    try:
        # Regular LLM response
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": request.message}],
            temperature=0
        )

        llm_response = response.choices[0].message
        answer_text = extract_answer(llm_response)

        return {"answer": answer_text}

    except Exception as e:
        logging.exception("Error in chat_endpoint")
        raise HTTPException(status_code=500, detail=str(e))
