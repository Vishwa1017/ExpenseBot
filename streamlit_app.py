import streamlit as st
from app.chat_service import ask_finance_bot

st.set_page_config(page_title="Expense Bot", page_icon="💰", layout="centered")

st.title("💰 Expense Bot")
st.caption("Ask questions about your transactions, spending, payments, and categories.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sql"):
            with st.expander("Generated SQL"):
                st.code(message["sql"], language="sql")
        if message.get("result"):
            with st.expander("Raw Result"):
                st.json(message["result"])

# Chat input
question = st.chat_input("Ask something like: What is my largest transaction in 2024?")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing your data..."):
            response = ask_finance_bot(question)

            answer = response.get("answer", "Something went wrong.")
            sql = response.get("sql")
            result = response.get("result")
            error = response.get("error")

            st.markdown(answer)

            if sql:
                with st.expander("Generated SQL"):
                    st.code(sql, language="sql")

            if result:
                with st.expander("Raw Result"):
                    st.json(result)

            if error:
                with st.expander("Error"):
                    st.error(error)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sql": sql,
        "result": result
    })