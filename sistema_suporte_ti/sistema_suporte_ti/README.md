# Sistema de Suporte TI

Protótipo inicial com Python, FastAPI, Jinja2, Groq (GPT-OSS-20B), Google Docs e Google Sheets.

## Tecnologias
- Python para backend, regras de negócio, integrações e processamento das interações.
- FastAPI para servidor e rotas.
- Jinja2 para renderização HTML no servidor.
- HTML e CSS para a interface.
- Não utiliza JavaScript.

## Preparação
1. Crie e ative um ambiente virtual Python.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Copie `.env.example` para `.env` e preencha as configurações.
4. Configure a conta de serviço Google e salve o JSON real em `credentials/google_service_account.json`.
5. Compartilhe o Google Docs e a planilha com o e-mail da conta de serviço.

## Executar
`uvicorn app.main:app --reload`

Acesse `http://127.0.0.1:8000/` para a interface e `/docs` para a documentação automática da API.

## Atenção
Este é um esqueleto inicial, não um sistema pronto para produção. A autenticação OAuth dos colaboradores,
o controle persistente de sessão/tentativas, a proteção contra duplicidade, a interface completa,
os testes automatizados e as políticas de autorização ainda precisam ser implementados.
Nunca versione `.env` nem credenciais reais.
