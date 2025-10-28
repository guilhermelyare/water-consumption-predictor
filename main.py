from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Sistema de Previsão de Consumo de Água",
    description="API para previsão de consumo baseada em clima e histórico",
    version="1.0"
)

app.include_router(endpoints.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
