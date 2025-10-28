from pydantic import BaseModel, Field
from typing import List

class PredictionInput(BaseModel):
    temperatura: float
    umidade: float
    chuva: float
    mes: int = Field(..., ge=1, le=12)
    ano: int

class PredictionResult(BaseModel):
    consumo_previsto: float
