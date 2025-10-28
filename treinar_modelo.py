import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.losses import MeanSquaredError
from keras.metrics import MeanAbsoluteError

# Carregar os dados simulados
df = pd.read_csv("dados_consumo_simulados.csv")

# Selecionar colunas de entrada e saída
X = df[['temperatura', 'umidade', 'chuva']]
y = df['consumo']

# Normalizar entradas
X = X / X.max()

# Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(3,)),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(
    optimizer="adam",
    loss=MeanSquaredError(),
    metrics=[MeanAbsoluteError()]
)

# Early stopping
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Treinar
model.fit(X_train, y_train, validation_data=(X_test, y_test),
          epochs=100, batch_size=16, callbacks=[early_stop], verbose=1)

# Avaliar
loss, mae = model.evaluate(X_test, y_test)
print(f"MAE: {mae:.2f}")

# Salvar modelo
model.save("app/data/model.h5")
print("Modelo salvo em app/data/model.h5")
