import sqlite3
from app.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_transactions_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_file TEXT,
        transaction_date TEXT,
        posting_date TEXT,
        year TEXT,
        description TEXT,
        amount REAL,
        category TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_transaction(record: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (source_file, transaction_date, posting_date, year, description, amount, category)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        record["source_file"],
        record["transaction_date"],
        record["posting_date"],
        record["year"],
        record["description"],
        record["amount"],
        record["category"]
    ))

    conn.commit()
    conn.close()

def run_query(sql: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] if cursor.description else []
    conn.close()
    return columns, rows