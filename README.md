📄 README.md para tu proyecto MNIST Trainer

# 🧠 Clasificador de Dígitos MNIST con Keras

Este proyecto entrena un modelo de red neuronal superficial para clasificar imágenes del dataset **MNIST** (dígitos manuscritos del 0 al 9) utilizando **Keras** con **TensorFlow** como backend.

El objetivo es disponer de un ejemplo sencillo, funcional y rápido de entrenar para entender el flujo básico de un proyecto de Machine Learning.

---

## 🛠️ Requisitos

- Python 3.10 o superior
- Entorno virtual recomendado

Instalar dependencias:

```bash
pip install -r requirements.txt

Estructura del proyecto
bash
Copiar código
mnist-classification-keras/
│
├── minst_trainer.py        # Script principal
├── requirements.txt        # Librerías necesarias
├── README.md                # Este archivo

🚀 Cómo ejecutar
Crear y activar un entorno virtual:

python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
Instalar dependencias:

pip install -r requirements.txt
Ejecutar el programa:

python minst_trainer.py
El modelo se entrenará durante 10 épocas y mostrará la precisión final alcanzada.

📈 Resultados esperados
Con esta arquitectura sencilla se puede alcanzar una precisión superior al 97% en el conjunto de prueba de MNIST.

📜 Notas adicionales
Si quieres guardar el modelo entrenado, descomenta la línea model.save('mnist_simple_model.keras').

El dataset MNIST se descarga automáticamente la primera vez que se ejecuta el script.

Esta implementación utiliza CPU; no es necesaria una GPU para este proyecto.

✨ Autor
Proyecto realizado por Angel Calvar Pastoriza como parte de mi formación práctica en Machine Learning.