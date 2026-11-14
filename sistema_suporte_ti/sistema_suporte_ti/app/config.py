import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
GOOGLE_DOC_ID = os.getenv("GOOGLE_DOC_ID", "")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "Chamados")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS",
    "credentials/google_service_account.json",
)
