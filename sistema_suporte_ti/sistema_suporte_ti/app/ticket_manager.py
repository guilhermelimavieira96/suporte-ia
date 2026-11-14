from datetime import datetime, timezone
from uuid import uuid4
from app.google_tools import append_ticket

def create_ticket(data: dict) -> str:
    required = ["name", "email", "description", "category", "summary", "priority"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValueError(f"Campos obrigatórios ausentes: {', '.join(missing)}")
    if data.get("confirmed") is not True:
        raise PermissionError("É necessária confirmação explícita do colaborador.")

    protocol = f"TI-{uuid4().hex[:8].upper()}"
    values = [
        protocol,
        data["name"],
        data["email"],
        data["description"],
        datetime.now(timezone.utc).isoformat(),
        "Aberto",
        data["category"],
        int(data.get("attempts", 0)),
        data["summary"],
        data["priority"],
    ]
    append_ticket(values)
    return protocol
