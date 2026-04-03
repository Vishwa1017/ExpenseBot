from fastapi import FastAPI
from pydantic import BaseModel

from app.chat_service import ask_finance_bot

app = FastAPI(title="Expense Bot API", version="1.0.0")


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    ok: bool
    question: str
    sql: str | None = None
    answer: str
    result: dict | None = None
    error: str | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = ask_finance_bot(request.question)
    return response