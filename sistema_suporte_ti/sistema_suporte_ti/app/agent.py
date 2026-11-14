from app.prompts import SYSTEM_PROMPT
from app.services.groq_service import ask_groq
from app.services.knowledge_service import get_knowledge

def answer_user(message: str, history: list | None = None) -> str:
    """Monta o contexto e solicita uma resposta ao modelo."""
    knowledge = get_knowledge()
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + "\n\nDocumentação:\n" + knowledge}
    ]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": message})
    return ask_groq(messages)
