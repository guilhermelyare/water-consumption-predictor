# 💧 Water Consumption Predictor  
### Sistema Inteligente de Previsão de Consumo de Água

Este projeto implementa um sistema inteligente para prever o **consumo mensal de água** com base em **dados climáticos (temperatura, umidade, chuva)** e **histórico de consumo**.  

A aplicação foi desenvolvida em **FastAPI** com um modelo de **Machine Learning (Keras/TensorFlow)** treinado em dados simulados.  

---

## 📌 Objetivo

O objetivo é demonstrar o uso de **Inteligência Artificial** na **gestão de recursos hídricos**, permitindo estimar o consumo com base em padrões climáticos e históricos.  


---

## 🧠 Estratégia de Treinamento do Modelo

### 🔬 Modelo
- **Tipo:** Rede Neural Artificial (MLP - Multilayer Perceptron)
- **Camadas:**
  - `Dense(64, activation='relu')`
  - `Dense(32, activation='relu')`
  - `Dense(1)` (saída contínua)
- **Perda:** Mean Squared Error (MSE)
- **Métrica:** Mean Absolute Error (MAE)
- **Divisão dos dados:** 80% treino / 20% validação
- **Normalização:** Entradas normalizadas entre 0 e 1
- **Parada antecipada:** EarlyStopping (pacote Keras)

### 📊 Dados
Os dados usados são **simulados** e representam:
- Temperatura média mensal (°C)
- Umidade relativa do ar (%)
- Chuva acumulada (mm)
- Consumo mensal de água (litros)

### 🧩 Fluxo de Treinamento
1. Carregamento do dataset `dados_consumo_simulados.csv`  
2. Normalização das colunas de entrada  
3. Separação em treino e teste  
4. Treinamento do modelo neural  
5. Salvamento do modelo em `app/data/model.h5`

---

## 🧠 Estratégia LLM Aplicada

Embora o modelo de previsão seja **um modelo tradicional de aprendizado supervisionado (ML)**, o projeto foi **planejado, documentado e otimizado com o apoio de um LLM (ChatGPT)**.

A LLM foi usada para:
- Refatoração e explicação de código  
- Estruturação da documentação técnica  
- Sugestão de boas práticas em IA aplicada  
- Escrita automatizada de README e schemas  

Isso demonstra o uso **híbrido e produtivo entre IA generativa e IA preditiva** no desenvolvimento do projeto.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.11+**  
- ⚙️ **FastAPI** — API backend  
- 🤖 **TensorFlow / Keras** — modelo preditivo  
- 🧮 **Pandas / NumPy / Scikit-learn** — manipulação e treino  
- 🧾 **Pydantic** — validação de dados  
- 🚀 **Uvicorn** — servidor local  
- 📘 **Postman** — testes da API  
- 🎨 **Figma** — protótipo da interface do usuário  

---


## 📁 Estrutura do Projeto

```
projeto_previsao_backend/
│
├── app/
│   ├── api/
│   │   └── endpoints.py          # Endpoints da API
│   ├── models/
│   │   └── predictor.py          # Carregamento e predição do modelo
│   ├── schemas/
│   │   └── inputs.py             # Estrutura de entrada e saída
│   ├── utils/
│   │   └── preprocessing.py      # Normalização de dados
│   └── data/
│       ├── model.h5              # Modelo treinado
│       └── historico.txt         # Histórico de previsões
│
├── main.py                       # Inicialização do FastAPI
├── treinar_modelo.py             # Script de treinamento
└── dados_consumo_simulados.csv   # Dataset de treino
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/water-consumption-predictor.git
cd water-consumption-predictor
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate   # (no Windows)
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Treine o modelo

```bash
python treinar_modelo.py
```

### 5. Inicie a API

```bash
uvicorn main:app --reload
```

> Acesse a documentação interativa (Swagger UI):  
👉 http://127.0.0.1:8000/docs

---

## 📡 Endpoints Disponíveis

### `POST /prever`

Faz a previsão de consumo de água e salva o resultado no histórico.

**Corpo da requisição:**

```json
{
  "temperatura": 28.5,
  "umidade": 65.0,
  "chuva": 3.2,
  "consumo_passado": [1200, 1100, 1300],
  "mes": 10,
  "ano": 2025
}
```

**Resposta:**

```json
{
  "consumo_previsto": 1243.56
}
```

---

### `GET /historico`

Retorna o histórico completo de previsões.

**Resposta:**

```json
{
  "historico": [
    {
      "ano": 2025,
      "mes": 10,
      "temperatura": 28.5,
      "umidade": 65.0,
      "chuva": 3.2,
      "consumo_previsto": 1243.56
    }
  ]
}
```

#### 🔎 Filtro opcional

Permite filtrar por `ano` e `mes`:

```
GET /historico?ano=2025&mes=10
```
