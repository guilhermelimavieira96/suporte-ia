from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.chat_routes import router as chat_router
from app.routes.ticket_routes import router as ticket_router

app = FastAPI(title="Sistema de Suporte TI")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(chat_router, prefix="/api")
app.include_router(ticket_router, prefix="/api")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

@app.get("/chat")
def chat_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={"request": request, "answer": None, "error": None},
    )

@app.get("/health")
def health():
    return {"status": "ok"}
