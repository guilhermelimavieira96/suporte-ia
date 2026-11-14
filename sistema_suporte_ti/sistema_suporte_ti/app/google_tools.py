from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from app import config

SCOPES = [
    "https://www.googleapis.com/auth/documents.readonly",
    "https://www.googleapis.com/auth/spreadsheets",
]

def get_google_credentials():
    path = Path(config.GOOGLE_APPLICATION_CREDENTIALS)
    if not path.exists():
        raise FileNotFoundError(f"Credenciais Google não encontradas: {path}")
    return service_account.Credentials.from_service_account_file(
        str(path), scopes=SCOPES
    )

def read_google_doc() -> str:
    if not config.GOOGLE_DOC_ID:
        raise ValueError("Configure GOOGLE_DOC_ID no arquivo .env")
    service = build("docs", "v1", credentials=get_google_credentials())
    document = service.documents().get(documentId=config.GOOGLE_DOC_ID).execute()

    chunks = []
    for item in document.get("body", {}).get("content", []):
        paragraph = item.get("paragraph", {})
        for element in paragraph.get("elements", []):
            text_run = element.get("textRun", {})
            chunks.append(text_run.get("content", ""))
    return "".join(chunks).strip()

def append_ticket(values: list):
    if not config.GOOGLE_SHEET_ID:
        raise ValueError("Configure GOOGLE_SHEET_ID no arquivo .env")
    service = build("sheets", "v4", credentials=get_google_credentials())
    range_name = f"{config.GOOGLE_SHEET_NAME}!A:J"
    body = {"values": [values]}
    return service.spreadsheets().values().append(
        spreadsheetId=config.GOOGLE_SHEET_ID,
        range=range_name,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body,
    ).execute()
