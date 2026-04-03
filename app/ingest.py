import json
import os
import re
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import ChatOpenAI

from app.config import STATEMENTS_DIR, MODEL_NAME
from app.db import create_transactions_table, insert_transaction
from app.prompts import EXTRACTION_PROMPT

load_dotenv()

def extract_year_from_filename(filename):
    match = re.search(r"(20\d{2})", filename)
    return match.group(1) if match else None

def ingest_all_statements():
    create_transactions_table()
    model = ChatOpenAI(model=MODEL_NAME, temperature=0)

    for file in os.listdir(STATEMENTS_DIR):
        if not file.endswith(".pdf"):
            continue

        print(f"Processing: {file}")
        file_path = STATEMENTS_DIR / file
        year = extract_year_from_filename(file)

        loader = PyMuPDFLoader(str(file_path))
        docs = loader.load()

        if not docs:
            print(f"Skipped {file}: no pages loaded")
            continue

        full_text = "\n\n".join(doc.page_content for doc in docs)
        prompt = EXTRACTION_PROMPT.format(statement_text=full_text)

        try:
            response = model.invoke(prompt)
            transactions = json.loads(response.content)
        except Exception as e:
            print(f"Skipped {file}: {e}")
            continue

        inserted = 0
        for t in transactions:
            try:
                record = {
                    "source_file": file,
                    "transaction_date": t["transaction_date"],
                    "posting_date": t["posting_date"],
                    "year": year,
                    "description": t["description"],
                    "amount": t["amount"],
                    "category": t.get("category", "Other"),
                }
                insert_transaction(record)
                inserted += 1
            except Exception as e:
                print(f"Bad row in {file}: {e}")

        print(f"Inserted {inserted} rows from {file}")