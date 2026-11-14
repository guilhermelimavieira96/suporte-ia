from openai import OpenAI
from app.config import GROQ_API_KEY, GROQ_MODEL

def ask_groq(messages: list[dict]) -> str:
    if not GROQ_API_KEY:
        raise RuntimeError("Configure GROQ_API_KEY no arquivo .env")
    client = OpenAI(
        api_key=GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1",
    )
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
    )
    return response.choices[0].message.content or ""
