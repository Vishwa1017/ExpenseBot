from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
STATEMENTS_DIR = DATA_DIR / "All_Statements"
DB_PATH = DATA_DIR / "transactions.db"

MODEL_NAME = "gpt-5-nano"