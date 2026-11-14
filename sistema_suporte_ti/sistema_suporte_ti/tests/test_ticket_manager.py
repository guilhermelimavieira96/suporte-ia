def test_confirmation_required():
    from app.ticket_manager import create_ticket
    data = {
        "name": "Teste", "email": "teste@example.com",
        "description": "Falha", "category": "Rede",
        "summary": "Falha de rede", "priority": "Média",
        "confirmed": False
    }
    try:
        create_ticket(data)
    except PermissionError:
        assert True
    else:
        assert False
