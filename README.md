# 🧱 Predicción de Resistencia del Concreto

Este es un sistema inteligente para predecir la resistencia a la compresión del concreto (en MPa) basado en sus componentes y la edad de curado, utilizando técnicas de Machine Learning.  
La aplicación está desarrollada con **Streamlit** y desplegada en **Streamlit Cloud**, ofreciendo una interfaz interactiva para predicciones y visualizaciones de datos.

---

## 📌 Descripción del Proyecto

### 🎯 Objetivo
Desarrollar un modelo predictivo para optimizar diseños de mezclas de concreto, asegurando calidad, durabilidad y eficiencia de costos en la construcción.

### 🧪 Metodología
- Análisis exploratorio de datos de componentes de concreto.
- Preprocesamiento de datos (normalización/escalado).
- Entrenamiento de modelos de regresión (`Random Forest`, `Gradient Boosting`, `SVR`).
- Evaluación y selección del mejor modelo según métricas de rendimiento.
- Implementación de una interfaz web con **Streamlit**.

### 💡 Importancia
Permite reducir costos, garantizar calidad y minimizar el impacto ambiental en la producción de concreto.

---

## 📂 Estructura de Notebooks

El proyecto se divide en tres notebooks principales:

### `NB1_EDA_Ortiz_Perez_Zamora.ipynb`
- **Objetivo:** Análisis exploratorio de datos (EDA).
- **Entrada:** `Concrete_Data.xls` (dataset original).
- **Salida:** `cleaned_concrete_data.csv` (dataset limpio).

### `NB2_MODELO_Ortiz_Perez_Zamora.ipynb`
- **Objetivo:** Ajuste de hiperparámetros y selección del mejor modelo.
- **Entrada:** `cleaned_concrete_data.csv`.
- **Salida:** `modelo.pkl` (modelo entrenado y serializado).

### `NB3_STREAMLIT_Ortiz_Perez_Zamora.ipynb`
- **Objetivo:** Integración del modelo en la interfaz web (Streamlit).
- **Entrada:** `Concrete_Data.xls` y `modelo.pkl`.

---

## 🛠️ Características del Proyecto

- **Pestaña de Predicción:**  
  Ingresa los valores de los componentes de la mezcla (cemento, escoria, ceniza volante, agua, superplastificante, agregados gruesos/finos y edad) para predecir la resistencia a la compresión.

- **Pestaña de Información:**  
  Detalles sobre los objetivos del proyecto, metodología, análisis de variables y rangos de aplicación.

- **Pestaña de Visualizaciones:**  
  Explora correlaciones, distribución de resistencia y relaciones entre cemento/edad y resistencia (requiere `Concrete_Data.xls`).

---

## ⚙️ Requisitos del Proyecto

### 📌 Python
- Python 3.x

### 📦 Librerías (en `requirements.txt`)
- `scikit-learn`  
- `plotly`  
- `pillow`  
- `opencv-python`  
- `matplotlib`  
- `seaborn`  
- `openpyxl`  
- `streamlit`  
- `pandas`  
- `numpy`  
- `xlrd`

### 🖥️ Dependencias del sistema (en `packages.txt`)
- `libgl1-mesa-glx`

---

## 🚀 Instrucciones de Uso

Accede a la aplicación en:  
🔗 [https://pfml-ortiz-perez-zamora.streamlit.app/](https://pfml-ortiz-perez-zamora.streamlit.app/)

---

## 🧪 Uso

1. **Predicción:**  
   Ingresa los valores de la mezcla en la pestaña "Predicción" y haz clic en **"Predecir resistencia"** para obtener la resistencia estimada, categoría y recomendaciones.

2. **Visualizaciones:**  
   Selecciona un tipo de visualización en la pestaña "Visualizaciones" para analizar el dataset (ej. matriz de correlación, histogramas).

3. **Información:**  
   Revisa detalles del proyecto, impacto de variables y rangos de resistencia del concreto en la pestaña "Información del Proyecto".

---

## 📊 Dataset

- **Fuente:**  
  Repositorio de Machine Learning de UCI – *Concrete Compressive Strength Data Set*.

- **Archivo:**  
  `Concrete_Data.xls` (contiene componentes de mezcla y valores de resistencia).

---

## 👥 Colaboradores

- Diego Mauricio Ortiz (22500445)  
- Daniel Felipe Zamora Pineda (22500225)  
- Jairo Andrés Pérez Hurtado (22500487)
