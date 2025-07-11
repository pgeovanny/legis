from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(
    title="Questões e Resumos SaaS",
    description="Backend avançado para extração inteligente, análise e exportação de questões de banca",
    version="1.0.0",
)

app.include_router(api_router)
