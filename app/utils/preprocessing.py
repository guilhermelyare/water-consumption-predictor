def preprocess_input(dados):
    return [
        dados.temperatura / 100,
        dados.umidade / 100,
        dados.chuva / 50
    ]
