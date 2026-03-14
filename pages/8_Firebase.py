import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

st.code("""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

# 1. Cargar las credenciales desde el archivo JSON
cred = credentials.Certificate("llave_secreta.json")

# 2. Inicializar la aplicación de Firebase
# (Se recomienda verificar si ya está inicializada para evitar errores en Streamlit)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# 3. Obtener el cliente de Firestore
db = firestore.client()

# 4. Acceder a la colección 'vehiculos' y obtener todos los documentos
docs = db.collection("vehiculos").stream()

# 5. Convertir los documentos a una lista de diccionarios
lista_vehiculos = [doc.to_dict() for doc in docs]

# 6. Crear el DataFrame final
df_firebase = pd.DataFrame(lista_vehiculos)

# 7. Mostrar el resultado (ejemplo)
# st.dataframe(df_firebase)

print("Conexión teórica a Firebase Firestore establecida")
""", language="python")



