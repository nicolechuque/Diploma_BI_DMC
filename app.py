import streamlit as st
#Ingreso de título
st.title("Proyecto Final Diploma BI")

st.sidebar.title("Parámetros")

st.image("Python_logo_and_wordmark.svg.png",width = 500)
st.sidebar.image("logo-secundario-dmc-institute-01.png",width = 300)

st.write("Elaborado por: Nicole Chuque")

archivo = st.file_uploader("Cargue el archivo excel o csv")

# Validamos si el usuario cargó un archivo

if archivo is not None:

 

    # Validamos si el archivo cargado tiene extensión .csv

    if archivo.name.endswith(".csv"):

 

        # Leemos el archivo CSV y lo guardamos en un DataFrame

        data = pd.read_csv(archivo)

 

        # Mostramos el DataFrame en la aplicación

        st.write(data.head())

 

    # Validamos si el archivo cargado tiene extensión .xlsx

    elif archivo.name.endswith(".xlsx"):

 

        # Leemos el archivo Excel y lo guardamos en un DataFrame

        data = pd.read_excel(archivo)

 

        # Mostramos el DataFrame en la aplicación

        st.write(data)

 

    # Si el archivo no es CSV ni Excel, mostramos un mensaje de error

    else:

        st.write("Formato no válido")

 

# Si el usuario no ha cargado ningún archivo, mostramos un mensaje

else:

    st.write("Por favor cargue su archivo")
