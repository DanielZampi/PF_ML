# 🧱 Predicción de Resistencia del Concreto

Aplicación desarrollada con técnicas de aprendizaje automático para predecir la resistencia a la compresión del concreto a partir de sus componentes y edad de curado. Implementada con **Streamlit** y disponible en la nube.

🔗 [Aplicación Web](https://pfml-ortiz-perez-zamora.streamlit.app/)  

---

## 🎯 Objetivo

Desarrollar un modelo de regresión supervisada que prediga la resistencia del concreto (MPa), facilitando decisiones técnicas, reduciendo costos y evitando ensayos destructivos.

---

## 📊 Dataset

- Fuente: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength)
- Observaciones: 1030  
- Variables: 8 predictoras + 1 objetivo (resistencia a la compresión)  
- Formato original: `Concrete_Data.xls`

---

## ⚙️ Pipeline del Proyecto

1. **EDA** (`NB1_EDA_Ortiz_Perez_Zamora.ipynb`)
   - Limpieza, visualización y análisis de datos.
   - Entrada: `Concrete_Data.xls`
   - Salida: `cleaned_concrete_data.csv`

2. **Modelado** (`NB2_MODELO_Ortiz_Perez_Zamora.ipynb`)
   - Comparación de modelos: Random Forest, SVR y Gradient Boosting.
   - Validación cruzada + ajuste de hiperparámetros.
   - Entrada: `cleaned_concrete_data.csv`
   - Salida: `modelo.pkl` 

3. **Despliegue** (`NB3_STREAMLIT_Ortiz_Perez_Zamora.ipynb`)
   - Carga del modelo y dataset.
   - Interfaz con Streamlit.
   - Etrada #1: `Concrete_Data.xls`
   - Entrada #2: `modelo.pkl`
   - Salida: `app.py`

---

## 🧪 Funcionalidades

- **Predicción:** Ingreso de variables y cálculo de resistencia estimada.
- **Visualización:** Histogramas, correlaciones y análisis exploratorio.
- **Información del proyecto:** Metodología, rangos de uso y datos clave.

---

## 📦 Requisitos

### Python
- Python 3.x

### Dependencias (`requirements.txt`)
- `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`,  
  `plotly`, `streamlit`, `openpyxl`, `xlrd`, `pillow`, `opencv-python`

### Sistema (`packages.txt`)
- `libgl1-mesa-glx`

---

## 👨‍💻 Colaboradores

- **Jairo Andrés Pérez Hurtado** (22500487)  
- **Daniel Felipe Zamora Pineda** (22500225)  
- **Diego Mauricio Ortiz** (22500445)

Profesor: **Sergio Alejandro Cantillo Luna**  
Universidad Autónoma de Occidente – Maestría en IA y Ciencia de Datos (2025)

---

## 📚 Referencias

- Yeh, I. C. (1998). *Modeling of strength of high-performance concrete using neural networks*. Cement and Concrete Research.  
- Chou et al. (2011). *Machine learning in concrete strength simulations*. Construction and Building Materials.
