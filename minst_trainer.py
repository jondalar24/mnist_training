# minst_trainer.py

# ==========================
# 1. Importar librerías necesarias
# ==========================

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.utils import to_categorical
import pandas as pd

# ==========================
# 2. Cargar el dataset desde archivo local
# ==========================

# Asegúrate que el archivo mnist_train.csv está en la raíz del proyecto
# Si prefieres trabajar con el mnist que viene en keras, se puede cambiar

from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# ==========================
# 3. Preprocesamiento
# ==========================

# Aplanar las imágenes
num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')

# Normalizar los píxeles
X_train /= 255
X_test /= 255

# One-hot encoding de las etiquetas
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

num_classes = y_test.shape[1]

# ==========================
# 4. Construir el modelo
# ==========================

def build_model():
    model = Sequential()
    model.add(Input(shape=(num_pixels,)))
    model.add(Dense(num_pixels, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    #Compila
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

model = build_model()

# ==========================
# 5. Entrenar el modelo
# ==========================

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)

# ==========================
# 6. Evaluar el modelo
# ==========================

scores = model.evaluate(X_test, y_test, verbose=0)
print('\nResultados finales:')
print(f"Precisión en test: {scores[1]*100:.2f}%")
print(f"Error en test: {(1-scores[1])*100:.2f}%")

# ==========================
# 7. Guardar el modelo (opcional)
# ==========================

# model.save('mnist_simple_model.keras')
