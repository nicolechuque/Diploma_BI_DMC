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

        # 1. Creamos las 6 pestañas obligatorias de tu rúbrica
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
            
            # Usamos st.columns para poner datos uno al lado del otro
            col1, col2, col3 = st.columns(3)
            col1.metric("Total de Filas", data.shape[0])
            col2.metric("Total de Columnas", data.shape[1])
            col3.metric("Filas Duplicadas", data.duplicated().sum())
            
            st.write("#### Vista previa de los datos:")
            st.dataframe(data.head(10))

        # ==========================================
        # TAB 2: ANÁLISIS UNIVARIADO
        # ==========================================
        with tab2:
            st.write("### Análisis de una sola variable")
            
            # Tus selectores que ya tenías creados
            lista_columna_numerica = data.select_dtypes(include="number").columns.tolist()
            if lista_columna_numerica:
                variable_num = st.selectbox("Seleccione una columna numérica para ver su distribución:", lista_columna_numerica, key="univ_num")
                
                # Ejemplo de Histograma (Código que usas en Colab adaptado a Streamlit)
                fig, ax = plt.subplots()
                sns.histplot(data[variable_num], kde=True, ax=ax, color="skyblue")
                ax.set_title(f"Histograma de {variable_num}")
                st.pyplot(fig) # <-- Así es como se muestra el gráfico en la web
            else:
                st.write("No hay columnas numéricas en este dataset.")

        # ==========================================
        # TAB 3: ANÁLISIS BIVARIADO
        # ==========================================
        with tab3:
            st.write("### Relación entre dos variables")
            
            lista_columna_categorica = data.select_dtypes(include=["object", "category"]).columns.tolist()
            
            if lista_columna_numerica and lista_columna_categorica:
                col_n = st.selectbox("Seleccione variable numérica:", lista_columna_numerica, key="biv_num")
                col_c = st.selectbox("Seleccione variable categórica:", lista_columna_categorica, key="biv_cat")
                
                # Ejemplo de Boxplot bivariado
                fig, ax = plt.subplots()
                sns.boxplot(x=data[col_c], y=data[col_n], ax=ax)
                plt.xticks(rotation=45)
                st.pyplot(fig)
            else:
                st.write("Se necesitan columnas numéricas y categóricas para este análisis.")

        # ==========================================
        # TAB 4: ANÁLISIS MULTIVARIADO
        # ==========================================
        with tab4:
            st.write("### Mapa de Calor de Correlaciones (Heatmap)")
            
            if len(lista_columna_numerica) > 1:
                # Código clásico de Colab para correlaciones
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(data[lista_columna_numerica].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
                st.pyplot(fig)
            else:
                st.write("Se necesitan al menos 2 columnas numéricas para calcular correlaciones.")

        # ==========================================
        # TAB 5: ANÁLISIS TEMPORAL
        # ==========================================
        with tab5:
            st.write("### Evolución en el tiempo")
            st.info("Si tu dataset contiene fechas, aquí puedes graficar líneas de tendencia (ej: ventas por mes).")
            # Nota: Si tu dataset no tiene fechas, puedes dejar un mensaje explicativo o un gráfico simple de líneas.

        # ==========================================
        # TAB 6: INSIGHTS
        # ==========================================
        with tab6:
            st.write("### Conclusiones y Hallazgos Clave")
            st.success("**Insight 1:** Escribe aquí la primera conclusión importante que descubriste al analizar los gráficos.")
            st.warning("**Insight 2:** Añade recomendaciones basadas en los patrones que viste en el mapa de calor o histogramas.")

         
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
