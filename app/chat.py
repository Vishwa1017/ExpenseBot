from app.db import run_query
from app.sql_agent import generate_sql, analyze_result

def start_chat():
    print("Expense chatbot ready. Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Bot: Bye")
            break

        sql = generate_sql(question)
        print(f"\nGenerated SQL:\n{sql};\n")

        try:
            columns, rows = run_query(sql)
            result = {"columns": columns, "rows": rows}
        except Exception as e:
            print(f"Bot: SQL error: {e}\n")
            continue

        answer = analyze_result(question, sql + ";", result)
        print(f"Bot: {answer}\n")