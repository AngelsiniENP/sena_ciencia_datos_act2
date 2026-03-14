import streamlit as st
import pandas as pd

st.title("Método 1: Juntando varias Series")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame agrupando información sobre **películas favoritas**.

1. Crea tres Series de Pandas diferentes:
    - Una serie llamada `titulos` con al menos 4 nombres de películas.
    - Una serie llamada `directores` con los directores de esas películas.
    - Una serie llamada `años` con el año de estreno.
2. Une estas tres series en un único DataFrame llamado `df_peliculas`, asignando nombres descriptivos a las columnas (por ejemplo: `Título`, `Director`, `Año de Estreno`).
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación
titulos = pd.Series(["Inception", "Interstellar", "The Dark Knight", "The Prestige"])
directores = pd.Series(["Christopher Nolan", "Christopher Nolan", "Christopher Nolan", "Christopher Nolan"])
años = pd.Series([2010, 2014, 2008, 2006])

# Uniendo las series en un DataFrame
df_peliculas = pd.DataFrame({
    'Título': titulos,
    'Director': directores,
    'Año de Estreno': años
})

# Mostrando el DataFrame
st.dataframe(df_peliculas)
