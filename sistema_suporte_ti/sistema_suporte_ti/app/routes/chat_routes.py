import logging

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.agent import answer_user

logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/chat", response_class=HTMLResponse)
def chat_form(request: Request, message: str = Form(...)):
    try:
        answer = answer_user(message)
        return templates.TemplateResponse(
            request=request,
            name="chat.html",
            context={
                "request": request,
                "answer": answer,
                "message": message,
                "error": None,
            },
        )
    except Exception:
        logger.exception("Falha ao processar solicitação de chat.")
        return templates.TemplateResponse(
            request=request,
            name="chat.html",
            context={
                "request": request,
                "answer": None,
                "error": "Não foi possível consultar o atendimento neste momento.",
                "message": message,
            },
            status_code=503,
        )
