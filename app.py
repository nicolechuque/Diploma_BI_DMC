import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Guardamos el dataset cargado
if "data" not in st.session_state:
    st.session_state.data = None
   
# Guardamos el nombre del archivo cargado
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None

#Ingreso de título
st.title("Proyecto Final Diploma BI")

st.sidebar.title("Parámetros")

st.image("Python_logo_and_wordmark.svg.png",width = 500)
st.sidebar.image("logo-secundario-dmc-institute-01.png",width = 300)

st.write("Elaborado por: Nicole Chuque")

modulos = st.sidebar.selectbox("Selecione un módulo", ["Home","Carga y perfil del dataset","Procesamiento de datos","Análisis visual"])

if modulos == "Home":
    st.write("Bienvenidos a la aplicación")

    if st.session_state.data is not None:
        st.success(f"Dataset cargado: {st.session_state.nombre_archivo}")
    else:
        st.info("Aún no se ha cargado ningún dataset.")

# ==============================

# MÓDULO CARGA Y PERFIL

# ==============================

 

elif modulos == "Carga y perfil del dataset":

 

    st.subheader("Carga y perfil del dataset")

 

    # Creamos un cargador de archivos para subir archivos Excel o CSV

    archivo = st.file_uploader(

        "Cargue el archivo Excel o CSV",

        type=["csv", "xlsx"]

    )

 

    # Validamos si el usuario cargó un archivo

    if archivo is not None:

 

        # Guardamos el nombre del archivo en session_state

        st.session_state.nombre_archivo = archivo.name

 

        # Validamos si el archivo cargado tiene extensión .csv

        if archivo.name.endswith(".csv"):

 

            # Leemos el archivo CSV y lo guardamos en session_state

            st.session_state.data = pd.read_csv(archivo)

 

        # Validamos si el archivo cargado tiene extensión .xlsx

        elif archivo.name.endswith(".xlsx"):

 

            # Leemos el archivo Excel y lo guardamos en session_state

            st.session_state.data = pd.read_excel(archivo)

 

        # Si el archivo no es CSV ni Excel, mostramos un mensaje de error

        else:

            st.error("Formato no válido")

 

        # Confirmamos que el archivo fue cargado

        st.success("Archivo cargado correctamente")

 

    # Si ya existe un dataset cargado, lo mostramos

    if st.session_state.data is not None:

 

        st.write(f"Archivo actual: **{st.session_state.nombre_archivo}**")

 

        st.subheader("Vista previa del dataset")

        st.dataframe(st.session_state.data)

 

        st.subheader("Perfil básico del dataset")

 

        # Número de filas y columnas

        st.write("Filas:", st.session_state.data.shape[0])

        st.write("Columnas:", st.session_state.data.shape[1])

 

        # Nombres de columnas

        st.write("Columnas del dataset:")

        st.write(st.session_state.data.columns.tolist())

 

        # Tipos de datos

        st.write("Tipos de datos:")

        st.write(st.session_state.data.dtypes)

 

        # Valores nulos

        st.write("Valores nulos por columna:")

        st.write(st.session_state.data.isnull().sum())

 

        # Estadística descriptiva

        st.write("Estadística descriptiva:")

        st.write(st.session_state.data.describe())

 

        # Botón para eliminar el dataset cargado

        if st.button("Eliminar dataset cargado"):

            st.session_state.data = None

            st.session_state.nombre_archivo = None

            st.rerun()

    else:

        st.write("Por favor cargue su archivo.")


# ==============================

# MÓDULO PROCESAMIENTO DE DATOS

# ==============================

 

elif modulos == "Procesamiento de datos":

 

    st.subheader("Procesamiento de datos")

 

    if st.session_state.data is not None:

 

        data = st.session_state.data

 

        st.write("Dataset disponible para procesamiento:")

        st.dataframe(data)

 

        st.write("Valores nulos por columna:")

        st.write(data.isnull().sum())

 

    else:

        st.warning("Primero debe cargar un dataset en el módulo " 
                   "'Carga y perfil del dataset'.")

# ==============================

# MÓDULO ANÁLISIS VISUAL

# ==============================

elif modulos == "Análisis visual":
    st.subheader("Análisis visual")

    if st.session_state.data is not None:
        data = st.session_state.data

        # Creamos las 6 pestañas obligatorias de tu rúbrica
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "Tab 1: Resumen", 
            "Tab 2: Análisis univariado", 
            "Tab 3: Análisis bivariado", 
            "Tab 4: Análisis multivariado", 
            "Tab 5: Análisis temporal", 
            "Tab 6: Insights"
        ])

        # ==========================================
        # TAB 1: RESUMEN
        # ==========================================
        with tab1:
            st.write("### Indicadores principales del Dataset")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total de Registros", data.shape[0])
            col2.metric("Total de Variables", data.shape[1])
            col3.metric("Filas Duplicadas", data.duplicated().sum())
            
            st.write("#### Muestra de los datos cargados:")
            st.dataframe(data.head(10))

        # ==========================================
        # TAB 2: ANÁLISIS UNIVARIADO
        # ==========================================
        with tab2:
            st.write("### Análisis Univariado: Distribución de Salarios")
            
            # Usamos la columna exacta: Average_Salary_USD
            if "Average_Salary_USD" in data.columns:
                st.write("#### Histograma de Salario Promedio (USD)")
                fig1, ax1 = plt.subplots()
                sns.histplot(data["Average_Salary_USD"], kde=True, ax=ax1, color="skyblue")
                ax1.set_title("Distribución de Average_Salary_USD")
                st.pyplot(fig1)
                plt.close(fig1)
            else:
                st.warning("No se encontró la columna 'Average_Salary_USD' en el archivo cargado.")

        # ==========================================
        # TAB 3: ANÁLISIS BIVARIADO
        # ==========================================
        with tab3:
            st.write("### Análisis Bivariado: Impacto de la IA por Industria")
            
            # 1. Gráfico de Boxplot: Salario por Industria
            if "Average_Salary_USD" in data.columns and "Industry" in data.columns:
                st.write("#### Boxplot de Salario Promedio por Industria")
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                sns.boxplot(x=data["Industry"], y=data["Average_Salary_USD"], ax=ax2)
                plt.xticks(rotation=90)
                st.pyplot(fig2)
                plt.close(fig2)
                
            # 2. Gráfico de Barras: Riesgo de IA por Industria (Basado en AI_Replacement_Risk)
            if "AI_Replacement_Risk" in data.columns and "Industry" in data.columns:
                st.write("#### Riesgo Promedio de Reemplazo por IA según la Industria")
                fig3, ax3 = plt.subplots(figsize=(10, 6))
                df_grouped = data.groupby("Industry")["AI_Replacement_Risk"].mean().reset_index()
                sns.barplot(x="Industry", y="AI_Replacement_Risk", data=df_grouped, ax=ax3, palette="Reds_r")
                plt.xticks(rotation=90)
                st.pyplot(fig3)
                plt.close(fig3)

        # ==========================================
        # TAB 4: ANÁLISIS MULTIVARIADO
        # ==========================================
        with tab4:
            st.write("### Análisis Multivariado: Riesgos vs Demanda Futura")
            
            # 1. Scatter plot obligatorio: AI_Replacement_Risk vs Future_Demand_Score
            if "AI_Replacement_Risk" in data.columns and "Future_Demand_Score" in data.columns:
                st.write("#### Scatter Plot: Riesgo de Reemplazo vs Puntuación de Demanda Futura")
                fig4, ax4 = plt.subplots()
                sns.scatterplot(x=data["AI_Replacement_Risk"], y=data["Future_Demand_Score"], ax=ax4, alpha=0.7, color="purple")
                ax4.set_title("AI_Replacement_Risk vs Future_Demand_Score")
                st.pyplot(fig4)
                plt.close(fig4)
            
            # 2. Heatmap de correlación corregido con columnas numéricas de tu lista
            st.write("#### Mapa de Calor de Correlaciones Numéricas")
            # Filtramos únicamente las columnas numéricas reales que correspondan a tu lista
            columnas_interes = [c for c in ["AI_Replacement_Risk", "Future_Demand_Score", "Average_Salary_USD", "Years_Experience", "Job_Growth_2030", "Performance_Score", "Job_Satisfaction"] if c in data.columns]
            
            if len(columnas_interes) > 1:
                fig5 = plt.figure(figsize=(8, 6))
                corr_matrix = data[columnas_interes].corr()
                sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
                st.pyplot(fig5)
                plt.close(fig5)
            else:
                st.write("Se necesitan más variables numéricas para el Mapa de Calor.")

        # ==========================================
        # TAB 5: ANÁLISIS TEMPORAL
        # ==========================================
        with tab5:
            st.write("### Análisis de Habilidades (Alternativa Temporal)")
            st.info("Dado que este dataset es transversal (representa una foto fija del año), analizamos las habilidades requeridas.")
            
            # Gráfico de barras de habilidades: Required_Skills
            if "Required_Skills" in data.columns:
                st.write("#### Top 10 Habilidades más Requeridas")
                fig6, ax6 = plt.subplots(figsize=(10, 5))
                data["Required_Skills"].value_counts().head(10).plot(kind='bar', ax=ax6, color='orange')
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig6)
                plt.close(fig6)

        # ==========================================
        # TAB 6: INSIGHTS
        # ==========================================
        with tab6:
            st.write("### Conclusiones y Hallazgos Clave")
            st.success("**Insight 1 (Riesgo por Industria):** Las industrias muestran variaciones drásticas en su `AI_Replacement_Risk`, lo que permite identificar los sectores más vulnerables a la automatización.")
            st.warning("**Insight 2 (Salarios y Futuro):** El cruce entre `Average_Salary_USD` y `Future_Demand_Score` ayuda a mapear si los trabajos mejor remunerados mantendrán su relevancia hacia el futuro.")

         
        st.write("Dataset disponible para análisis visual:")

        st.dataframe(data)

        lista_columna_numerica = data.select_dtypes(include = "number").columns.tolist()
    
        variable_numerica = st.selectbox("Selecione la columna númerica",lista_columna_numerica)
    
     
    
        lista_columna_categorica = data.select_dtypes(include=["object", "category"]).columns.tolist()
    
        variable_categorica = st.selectbox("Seleccione la columna categórica",lista_columna_categorica)


    else:

        st.warning(

            "Primero debe cargar un dataset en el módulo "

            "'Carga y perfil del dataset'.")
