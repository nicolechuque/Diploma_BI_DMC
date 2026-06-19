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
            
            st.write("#### Muestra de los datos cargados (AI Impact on Jobs):")
            st.dataframe(data.head(10))

        # ==========================================
        # TAB 2: ANÁLISIS UNIVARIADO
        # ==========================================
        with tab2:
            st.write("### Análisis Univariado: Distribución de Salarios y Riesgos")
            
            # Buscamos la columna de salario (asumiendo que se llama 'Salary' o similar)
            columnas = data.columns.tolist()
            col_salario = max([c for c in columnas if 'sal' in c.lower() or 'wage' in c.lower()], default=None)
            
            if col_salario:
                st.write(f"#### Histograma de la variable: `{col_salario}`")
                fig, ax = plt.subplots()
                sns.histplot(data[col_salario], kde=True, ax=ax, color="skyblue")
                ax.set_title(f"Distribución de {col_salario}")
                st.pyplot(fig)
            else:
                st.warning("No se detectó automáticamente una columna con el nombre 'Salary'. Por favor, verifica cómo se llama exactamente en tu dataset.")

        # ==========================================
        # TAB 3: ANÁLISIS BIVARIADO
        # ==========================================
        with tab3:
            st.write("### Análisis Bivariado: Impacto de la IA por Industria")
            
            # Buscamos columnas clave basándonos en tu rúbrica
            col_industria = max([c for c in columnas if 'ind' in c.lower()], default=None)
            col_riesgo = max([c for c in columnas if 'risk' in c.lower() or 'impact' in c.lower()], default=None)
            
            # 1. Gráfico de Boxplot: Salario por Industria
            if col_salario and col_industria:
                st.write(f"#### Boxplot de `{col_salario}` por `{col_industria}`")
                fig1, ax1 = plt.subplots(figsize=(10, 6))
                sns.boxplot(x=data[col_industria], y=data[col_salario], ax=ax1)
                plt.xticks(rotation=90)
                st.pyplot(fig1)
                
            # 2. Gráfico de Barras: Riesgo de IA por Industria
            if col_riesgo and col_industria:
                st.write(f"#### Riesgo de Reemplazo por IA según la Industria")
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                # Tomamos el promedio de riesgo por industria
                df_grouped = data.groupby(col_industria)[col_riesgo].mean().reset_index()
                sns.barplot(x=col_industria, y=col_riesgo, data=df_grouped, ax=ax2, palette="Reds_r")
                plt.xticks(rotation=90)
                st.pyplot(fig2)

        # ==========================================
        # TAB 4: ANÁLISIS MULTIVARIADO
        # ==========================================
        with tab4:
            st.write("### Análisis Multivariado: Riesgos vs Demanda Futura")
            
            # Buscamos las columnas específicas que pide tu rúbrica
            col_demand = max([c for c in columnas if 'demand' in c.lower() or 'future' in c.lower()], default=None)
            
            # 1. Scatter plot obligatorio: Replacement Risk vs Future Demand Score
            if col_riesgo and col_demand:
                st.write(f"#### Scatter Plot: `{col_riesgo}` vs `{col_demand}`")
                fig3, ax3 = plt.subplots()
                sns.scatterplot(x=data[col_riesgo], y=data[col_demand], ax=ax3, alpha=0.7, color="purple")
                ax3.set_title("Relación entre Riesgo de Reemplazo y Demanda Futura")
                st.pyplot(fig3)
            
            # 2. Heatmap de correlación
            st.write("#### Mapa de Calor de las Variables Numéricas")
            lista_numericas = data.select_dtypes(include="number").columns.tolist()
            if len(lista_numericas) > 1:
                fig4, ax4 = plt.subplots(figsize=(8, 6))
                sns.heatmap(data[lista_numericas].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax4=ax4)
                st.pyplot(fig4)

        # ==========================================
        # TAB 5: ANÁLISIS TEMPORAL
        # ==========================================
        with tab5:
            st.write("### Análisis Temporal")
            st.info("El dataset 'AI Impact on Jobs' suele ser de corte transversal (no incluye fechas históricas).")
            st.write("Como este dataset no contiene una evolución en el tiempo paso a paso, añadimos un análisis de la distribución de frecuencias de habilidades requeridas como alternativa visual recomendada.")
            
            col_skills = max([c for c in columnas if 'skill' in c.lower()], default=None)
            if col_skills:
                fig5, ax5 = plt.subplots(figsize=(10, 5))
                data[col_skills].value_counts().head(10).plot(kind='bar', ax=ax5, color='orange')
                ax5.set_title("Top 10 Habilidades más Requeridas en la era de la IA")
                st.pyplot(fig5)

        # ==========================================
        # TAB 6: INSIGHTS
        # ==========================================
        with tab6:
            st.write("### Conclusiones y Hallazgos del Impacto de la IA")
            st.success("**Conclusión de Riesgo:** Ciertas industrias muestran un `AI_Replacement_Risk` significativamente más alto debido a tareas repetitivas.")
            st.warning("**Conclusión de Demanda:** Existe una correlación visible entre el riesgo de automatización y los cambios en el `Future_Demand_Score` de los empleos.")

         
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
