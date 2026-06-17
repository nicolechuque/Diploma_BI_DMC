import streamlit as st
#Ingreso de título
st.title("Proyecto Final Diploma BI")

st.sidebar.title("Parámetros")

st.image("Python_logo_and_wordmark.svg.png",width = 500)
st.sidebar.image("logo-secundario-dmc-institute-01.png",width = 300)

st.write("Elaborado por: Nicole Chuque")

archivo = st.file_uploader("Cargue el archivo excel o csv")

if archivo is not None :
  
  if archivo.name.endswith(".csv")
      data = pd. read_csv(archivo)
      st.write(data)
  elif archivo.name.endswith(".xlsx")
     data = pd. read_csv(archivo)
      st.write(data)
  else:
    st.write("Formato no válido")
    
else :
  st.write("Por favor cargue su archivo")
