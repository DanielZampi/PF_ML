import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Configuración de la página
st.set_page_config(page_title="Predicción de Resistencia del Concreto", layout="wide")

# Título y descripción
st.title("Sistema Inteligente de Predicción de Resistencia del Concreto")
st.markdown("""
Esta aplicación utiliza un modelo de Machine Learning para predecir la resistencia a la compresión del concreto (en MPa)
a partir de sus componentes y la edad de curado. El modelo fue entrenado con datos reales de mezclas de concreto.
""")

# Cargar modelo y escalador
#@st.cache_resource
#def cargar_modelo():
 #   modelo = joblib.load('best_concrete_model_Gradient_Boosting.joblib')
  #  return modelo

@st.cache_resource
def cargar_modelo():
    with open('modelo.pkl', 'rb') as f:
        modelo = pickle.load(f)
    return modelo

modelo = cargar_modelo()

# Crear pestañas
tab1, tab2, tab3 = st.tabs(["Predicción", "Información del Proyecto", "Visualizaciones"])

# Pestaña 1: Predicción
with tab1:
    st.header("Ingrese los valores de la mezcla:")

    # Crear dos columnas para los inputs
    col1, col2 = st.columns(2)

    with col1:
        cement = st.number_input("Cemento (kg/m³)", min_value=0.0, max_value=1000.0, value=350.0)
        slag = st.number_input("Escoria de alto horno (kg/m³)", min_value=0.0, max_value=400.0, value=0.0)
        fly_ash = st.number_input("Ceniza volante (kg/m³)", min_value=0.0, max_value=300.0, value=0.0)
        water = st.number_input("Agua (kg/m³)", min_value=100.0, max_value=300.0, value=180.0)

    with col2:
        superplasticizer = st.number_input("Superplastificante (kg/m³)", min_value=0.0, max_value=30.0, value=5.0)
        coarse_agg = st.number_input("Agregado grueso (kg/m³)", min_value=500.0, max_value=1200.0, value=1000.0)
        fine_agg = st.number_input("Agregado fino (kg/m³)", min_value=500.0, max_value=1000.0, value=800.0)
        age = st.number_input("Edad (días)", min_value=1, max_value=365, value=28)

    # Botón para predecir
    if st.button("Predecir resistencia"):
        # Crear DataFrame con los datos de entrada
        input_data = pd.DataFrame({
            'Cement': [cement],
            'Blast_Furnace_Slag': [slag],
            'Fly_Ash': [fly_ash],
            'Water': [water],
            'Superplasticizer': [superplasticizer],
            'Coarse_Aggregate': [coarse_agg],
            'Fine_Aggregate': [fine_agg],
             'Age': [age]
        })

        # Realizar la predicción
        prediction = modelo.predict(input_data)[0]

        # Mostrar resultado con estilo
        st.success(f"La resistencia estimada del concreto es: {prediction:.2f} MPa (Megapascales)")

        # Evaluación de la resistencia
        if prediction < 20:
            categoria = "Baja resistencia"
            recomendacion = ( "Considere aumentar el contenido de cemento o reducir la relación agua/cemento.\n"
                              "Ejemplos de uso: concreto para rellenos, bases temporales o estructuras no estructurales.\n"
                              "No recomendado para elementos que soporten cargas importantes."
                            )
        elif prediction < 40:
            categoria = "Resistencia moderada"
            recomendacion = ( "Adecuado para estructuras convencionales como viviendas, aceras y pavimentos.\n"
                              "Puede usarse en columnas, vigas y losas con cargas moderadas.\n"
                              "Revise siempre las especificaciones del proyecto para asegurar cumplimiento."
                            )
        else:
            categoria = "Alta resistencia"
            recomendacion = ( "Excelente para estructuras que requieren alta durabilidad y resistencia, como puentes, edificios altos y estructuras industriales.\n"
                              "Ideal para ambientes agresivos o con cargas elevadas.\n"
                              "Asegúrese de mantener un control riguroso de calidad en la mezcla y curado."
                            )

        # Mostrar evaluación
        st.info(f"Categoría: {categoria}")
        st.info(f"Recomendación: {recomendacion}")

        # Mostrar gráfico de medidor
        fig, ax = plt.subplots(figsize=(10, 2))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)
        ax.set_title("Escala de Resistencia (MPa)")
        ax.set_xticks([0, 20, 40, 60, 80, 100])
        ax.set_yticks([])
        ax.axvspan(0, 20, color='red', alpha=0.3)
        ax.axvspan(20, 40, color='yellow', alpha=0.3)
        ax.axvspan(40, 100, color='green', alpha=0.3)
        ax.axvline(prediction, color='blue', linewidth=4)
        ax.text(prediction, 0.5, f"{prediction:.1f}",
                horizontalalignment='center', verticalalignment='center',
                bbox=dict(facecolor='white', alpha=0.8))
        st.pyplot(fig)

# Pestaña 2: Información del Proyecto
with tab2:
    st.header("Acerca del Proyecto")
    st.markdown("""
    ### Objetivo
    Este proyecto tiene como objetivo desarrollar un sistema inteligente para predecir la resistencia a la compresión del concreto
    basado en sus componentes y edad de curado, utilizando técnicas de Machine Learning.

    ### Metodología
    1. **Análisis exploratorio de datos** para entender las relaciones entre variables
    2. **Preprocesamiento de datos** mediante normalización y escalado
    3. **Entrenamiento de modelos** de regresión (Random Forest, Gradient Boosting, Support Vector (SVR))
    4. **Evaluación y selección** del mejor modelo según métricas de rendimiento
    5. **Implementación** en una interfaz web con Streamlit

    ### Importancia
    La predicción precisa de la resistencia del concreto permite:
    - Optimizar las mezclas para reducir costos y mejorar la eficiencia
    - Asegurar la calidad y durabilidad de las estructuras construidas
    - Minimizar el impacto ambiental al reducir el uso innecesario de cemento
    - Agilizar el proceso de diseño y validación de mezclas en la industria de la construcción

    ### Interpretación del Modelo y Aplicaciones

    #### Análisis de Variables

    - MPa (Megapascal): es una unidad de presión del Sistema Internacional de Unidades, comúnmente utilizada en ingeniería
    para expresar la resistencia a la compresión de materiales como el concreto.
    - Un MPa equivale a un millón de pascales, y un pascal se define como un newton por metro cuadrado (N/m²): 1 MPa = 1,000,000 Pa = 1,000,000 N/m²
    - En el contexto del concreto la resistencia a la compresión medida en MPa indica cuánta presión puede soportar el material antes de fallar.
    Además, en unidades más prácticas para ingeniería civil:1 MPa ≈ 10.2 kg/cm²

    - **Cemento (β₁ = 0.12):** Cada kg/m³ de cemento aumenta la resistencia en aproximadamente 0.12 MPa, reflejando su papel crítico.
    - **Escoria (β₂ = 0.08):** Contribuye menos que el cemento, pero mejora la resistencia, especialmente a largo plazo.
    - **Ceniza volante (β₃ = 0.07):** Similar a la escoria, con un impacto ligeramente menor.
    - **Agua (β₄ = -0.15):** Un coeficiente negativo refleja que más agua reduce la resistencia debido a una mayor relación agua-cemento.
    - **Superplastificante (β₅ = 0.5):** Tiene un impacto positivo significativo al mejorar la trabajabilidad y reducir el agua necesaria.
    - **Agregado grueso (β₆ = 0.01) y Agregado fino (β₇ = 0.01):** Impacto mínimo, ya que los agregados afectan más la estructura que la resistencia directa.
    - **Edad (β₈ = 0.2):** Cada día de curado aumenta la resistencia en 0.2 MPa, reflejando el proceso de hidratación.

    #### Ejemplo de Cálculo

    Supongamos que tenemos una mezcla de concreto con los siguientes valores:
    - Cemento: 300 kg/m³
    - Escoria: 100 kg/m³
    - Ceniza volante: 50 kg/m³
    - Agua: 180 kg/m³
    - Superplastificante: 10 kg/m³
    - Agregado grueso: 1000 kg/m³
    - Agregado fino: 800 kg/m³
    - Edad: 28 días

    Sustituyendo en la ecuación:

    - f' = –20 + (0.12 * cemento) + (0.08 * escoria) + (0.07 * ceniza_volante) - (0.15 * agua) + (0.5 * superplastificante) + (0.01 * agregado_grueso) + (0.01 * agregado_fino) + (0.2 * edad)
    - f' = –20 + (0.12 × 300) + (0.08 × 100) + (0.07 × 50) – (0.15 × 180) + (0.5 × 10) + (0.01 × 1000) + (0.01 × 800) + (0.2 × 28)
    - f' = –20 + 36 + 8 + 3.5 – 27 + 5 + 10 + 8 + 5.6
    - f' = –20 + 76.1 = 56.1 MPa

    La resistencia estimada es 56.1 MPa, lo que indica un concreto adecuado para **puentes o infraestructura crítica.
    Lo que significa que el concreto puede soportar 56.1 millones de pascales de presión antes de romperse.

    #### Rangos de Resistencia del Concreto por Uso

    La resistencia a la compresión del concreto se mide a los 28 días de curado (edad estándar) y se expresa como resistencia característica (f') o resistencia promedio. Valores típicos por aplicación:

    1. **Edificios residenciales (viviendas, apartamentos):**
      - Rango: 20–35 MPa
      - Uso: Muros, losas, columnas en edificaciones de pocos pisos. Valor común: 25 MPa.

    2. **Edificios comerciales o de oficinas (múltiples pisos):**
      - Rango: 30–40 MPa
      - Uso: Requieren mayor resistencia para cargas elevadas. Valor típico: 35 MPa.

    3. **Puentes y viaductos:**
      - Rango: 35–50 MPa
      - Uso: Alta resistencia y durabilidad por cargas dinámicas y exposición ambiental. Valor común: 40–45 MPa.

    4. **Infraestructura crítica (presas, túneles, estructuras nucleares):**
      - Rango: 50–70 MPa o más
      - Uso: Alta resistencia y durabilidad extrema. En casos especiales puede superar los 100 MPa.

    5. **Estructuras prefabricadas o elementos especiales:**
      - Rango: 40–60 MPa
      - Uso: Vigas pretensadas o paneles que requieren eficiencia y seguridad.

    6. **Concreto ligero (aislamiento o cargas mínimas):**
      - Rango: 15–25 MPa
      - Uso: Estructuras donde el peso es crítico, pero con menor resistencia mecánica.

    ### Desarrollado por:
    - Diego Mauricio Ortiz Codigo: 22500445
    - Daniel Felipe Zamora Pineda Codigo: 22500225
    - Jairo Andrés Pérez Hurtatis Codigo: 22500487

    Estudiantes de la Maestría en Inteligencia Artificial y Ciencia de Datos
    """)

# Pestaña 3: Visualizaciones
with tab3:
    st.header("Visualizaciones")

    # Cargar datos de ejemplo para visualizaciones
    @st.cache_data
    def cargar_datos():
        try:
            return pd.read_excel('Concrete_Data.xls')
        except:
            st.error("No se pudo cargar el dataset. Las visualizaciones no están disponibles.")
            return None

    datos = cargar_datos()

    if datos is not None:
        # Selector de visualización
        viz_option = st.selectbox(
            "Seleccione una visualización:",
            ["Correlación entre variables", "Distribución de la resistencia", "Relación cemento-resistencia", "Relación edad-resistencia"]
        )

        if viz_option == "Correlación entre variables":
            st.subheader("Matriz de Correlación")
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(datos.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
            st.pyplot(fig)

        elif viz_option == "Distribución de la resistencia":
            st.subheader("Distribución de la Resistencia del Concreto")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(datos['Concrete compressive strength(MPa, megapascals) '], kde=True, ax=ax)
            ax.set_xlabel("Resistencia (MPa)")
            ax.set_ylabel("Frecuencia")
            st.pyplot(fig)

        elif viz_option == "Relación cemento-resistencia":
            st.subheader("Relación entre Cemento y Resistencia")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(x=datos['Cement (component 1)(kg in a m^3 mixture)'],
                           y=datos['Concrete compressive strength(MPa, megapascals) '], ax=ax)
            ax.set_xlabel("Contenido de Cemento (kg/m³)")
            ax.set_ylabel("Resistencia (MPa)")
            st.pyplot(fig)

        elif viz_option == "Relación edad-resistencia":
            st.subheader("Relación entre Edad y Resistencia")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x=datos['Age (day)'], y=datos['Concrete compressive strength(MPa, megapascals) '], ax=ax)
            ax.set_xlabel("Edad (días)")
            ax.set_ylabel("Resistencia (MPa)")
            st.pyplot(fig)

# Pie de página
st.write("---")
st.write("Desarrollado para el proyecto final de la asignatura de Machine Learning - Maestría en IA y Ciencia de Datos Junio de 2025")
