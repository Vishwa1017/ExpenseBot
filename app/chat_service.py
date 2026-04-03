from app.db import run_query
from app.sql_agent import generate_sql, analyze_result


def ask_finance_bot(question: str) -> dict:
    sql = generate_sql(question)

    try:
        columns, rows = run_query(sql)
        result = {"columns": columns, "rows": rows}
    except Exception as e:
        return {
            "ok": False,
            "question": question,
            "sql": sql,
            "error": str(e),
            "answer": "There was an error while querying the database."
        }

    answer = analyze_result(question, sql + ";", result)

    return {
        "ok": True,
        "question": question,
        "sql": sql,
        "result": result,
        "answer": answer
    }