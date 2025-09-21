from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.llm import router as llm_router

app = FastAPI(title="Graduate Employment Chatbot")

# Enable CORS so frontend can fetch API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(llm_router, prefix="/chat", tags=["chat"])

@app.get("/health")
def health():
    return {"status": "ok"}
