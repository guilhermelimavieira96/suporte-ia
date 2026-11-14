from app.google_tools import read_google_doc

def get_knowledge() -> str:
    """Obtém a documentação interna no Google Docs."""
    return read_google_doc()
