from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.ticket_manager import create_ticket

router = APIRouter()

class TicketRequest(BaseModel):
    name: str
    email: EmailStr
    description: str
    category: str
    attempts: int = 0
    summary: str
    priority: str
    confirmed: bool

@router.post("/tickets")
def create_ticket_route(payload: TicketRequest):
    try:
        protocol = create_ticket(payload.model_dump())
        return {"protocol": protocol, "status": "Aberto"}
    except (ValueError, PermissionError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Não foi possível registrar o chamado.") from exc
