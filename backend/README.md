# Backend SaaS Avançado para Questões de Banca e Resumos

Projeto FastAPI completo para extração, análise e exportação de questões de banca, com geração de resumos inteligentes.

## Como rodar

1. Copie o arquivo .env.example para .env e ajuste as variáveis.
2. Rode:
    docker-compose up --build
3. Acesse a documentação em http://localhost:8000/docs

Para rodar localmente (fora do Docker), instale as dependências e execute:
    uvicorn app.main:app --reload

## Principais funcionalidades

- Upload e extração inteligente de questões (PDF, DOCX, CSV, TXT)
- Análise do padrão da banca (pronto para IA)
- Geração de resumo inteligente (pronto para IA)
- Exportação para Word e PDF
- Gerenciamento de usuário, projeto e histórico
- Testes automatizados
- Documentação automática Swagger

