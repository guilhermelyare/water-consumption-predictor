from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Sistema de Previsão de Consumo de Água",
    description="API para previsão de consumo baseada em clima e histórico",
    version="1.0"
)

app.include_router(endpoints.router)