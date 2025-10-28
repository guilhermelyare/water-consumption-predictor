from fastapi import APIRouter
from app.models.predictor import predict_consumption
from app.schemas.inputs import PredictionInput, PredictionResult
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/prever", response_model=PredictionResult)
def fazer_previsao(dados: PredictionInput):
    resultado = predict_consumption(dados)
    return resultado

from fastapi import Query

@router.get("/historico")
def obter_historico(
    ano: int = Query(None, description="Ano desejado (ex: 2025)"),
    mes: int = Query(None, ge=1, le=12, description="Mês desejado (1 a 12)")
):
    historico_path = "app/data/historico.txt"
    historico_estruturado = []

    try:
        with open(historico_path, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(" | ")
                if len(partes) != 5:
                    continue

                ano_mes = partes[0].split("-")
                ano_reg = int(ano_mes[0])
                mes_reg = int(ano_mes[1])

                if ano and ano != ano_reg:
                    continue
                if mes and mes != mes_reg:
                    continue

                temperatura = float(partes[1].split(":")[1].strip())
                umidade = float(partes[2].split(":")[1].strip())
                chuva = float(partes[3].split(":")[1].strip())
                consumo = float(partes[4].split(":")[1].strip())

                historico_estruturado.append({
                    "ano": ano_reg,
                    "mes": mes_reg,
                    "temperatura": temperatura,
                    "umidade": umidade,
                    "chuva": chuva,
                    "consumo_previsto": consumo
                })

        return {"historico": historico_estruturado}

    except FileNotFoundError:
        return {"historico": []}

