import numpy as np
from keras.models import load_model
from app.utils.preprocessing import preprocess_input
import os


model = load_model("app/data/model.h5")

def predict_consumption(dados):
    X = preprocess_input(dados)
    y_pred = model.predict(np.array([X]))
    previsao = float(y_pred[0][0])

    # Montar linha de histórico
    linha = f"{dados.ano}-{dados.mes:02d} | Temp: {dados.temperatura} | Umid: {dados.umidade} | Chuva: {dados.chuva} | Consumo Previsto: {previsao:.2f}\n"
    
    # Criar pasta se não existir
    os.makedirs("app/data", exist_ok=True)

    # Salvar no histórico
    with open("app/data/historico.txt", "a", encoding="utf-8") as f:
        f.write(linha)

    return {"consumo_previsto": previsao}