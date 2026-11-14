import logging

from fastapi.testclient import TestClient

from app.main import app
from app.routes import chat_routes


def test_chat_returns_answer(monkeypatch):
    monkeypatch.setattr(chat_routes, "answer_user", lambda message: "Resposta de teste")

    response = TestClient(app).post("/api/chat", data={"message": "Preciso de ajuda"})

    assert response.status_code == 200
    assert "Resposta de teste" in response.text


def test_chat_logs_failure_and_returns_service_unavailable(monkeypatch, caplog):
    def fail_to_answer(message):
        raise RuntimeError("Erro de integração de teste")

    monkeypatch.setattr(chat_routes, "answer_user", fail_to_answer)

    with caplog.at_level(logging.ERROR, logger="app.routes.chat_routes"):
        response = TestClient(app).post("/api/chat", data={"message": "Preciso de ajuda"})

    assert response.status_code == 503
    assert "Não foi possível consultar o atendimento neste momento." in response.text
    assert "Falha ao processar solicitação de chat." in caplog.text
    assert "Erro de integração de teste" in caplog.text
