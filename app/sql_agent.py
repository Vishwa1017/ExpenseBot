from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.config import MODEL_NAME
from app.prompts import SQL_PROMPT, ANALYSIS_PROMPT

load_dotenv()

llm = ChatOpenAI(model=MODEL_NAME, temperature=0)

def generate_sql(question: str) -> str:
    prompt = SQL_PROMPT.format(question=question)
    response = llm.invoke(prompt)
    return response.content.strip().rstrip(";")

def analyze_result(question: str, sql: str, result: dict) -> str:
    prompt = ANALYSIS_PROMPT.format(
        question=question,
        sql=sql,
        result=result
    )
    response = llm.invoke(prompt)
    return response.content.strip()