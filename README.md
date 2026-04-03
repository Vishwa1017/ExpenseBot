---

![Demo](https://github.com/user-attachments/assets/f42edcc7-cdb5-4a79-89ca-4c369a5878b6)

https://github.com/user-attachments/assets/0cbfda5d-dc12-4bbe-b482-636dc9265b25

---

## 🧠 Example Questions

- What is my largest transaction?
- How much did I spend in 2024?
- Show my top 5 expenses
- How much did I spend on food?
- What are my biggest bills?

---

## 🏗️ Architecture


PDF Statements
↓
LLM Extraction (LangChain)
↓
Structured Transactions
↓
SQLite Database
↓
LLM → SQL Generation
↓
Query Execution
↓
LLM → Insight Generation
↓
Streamlit Chat UI


---

## ⚙️ Tech Stack

- **LangChain** – LLM orchestration  
- **OpenAI GPT Models** – extraction + reasoning  
- **SQLite** – structured storage  
- **Streamlit** – frontend UI  
- **PyMuPDF** – PDF parsing  
- **Python** – backend  

---

## 📂 Project Structure


MyExpenseBot/
│
├── app/
│ ├── ingest.py # PDF → structured data
│ ├── db.py # SQLite operations
│ ├── prompts.py # LLM prompts
│ ├── sql_agent.py # SQL generation
│ ├── chat_service.py # Orchestration logic
│
├── data/
│ ├── All_Statements/ # (ignored - add your PDFs here)
│ └── transactions.db
│
├── scripts/
│ ├── run_ingest.py
│
├── streamlit_app.py # Chat UI
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ExpenseBot.git
cd ExpenseBot
2. Install dependencies
pip install -r requirements.txt
3. Set up environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
4. Add your statements

Place your PDFs inside:

data/All_Statements/
5. Ingest data
python -m scripts.run_ingest
6. Start chatbot UI
streamlit run streamlit_app.py
🔐 Data Privacy
Bank statements are NOT stored in this repo
.gitignore excludes all personal financial data
Users must provide their own PDFs locally
⚠️ Limitations
Date format currently uses FEB 12 (not full ISO format)
Merchant normalization can be improved
Category classification is LLM-based (can be inconsistent)
🚀 Roadmap
 Normalize dates (YYYY-MM-DD)
 Merchant standardization (Walmart, McDonald's grouping)
 Monthly & trend analysis
 SQL validation + retry system
 Deployment (Streamlit Cloud)
 Improved UI + charts
💡 Key Learnings
Structured data > pure RAG for financial analysis
LLMs are powerful for:
extraction
SQL generation
explanation
SQLite enables accurate, fast, deterministic queries
🤝 Contributing

Open to improvements, ideas, and optimizations.
