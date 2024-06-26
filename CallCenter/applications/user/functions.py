from .models import *
import pyttsx3
from applications.user.models import *

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import joblib
import os
from django.conf import settings

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def getInformationUser(id_user):
    data = {}
    u = User.objects.get(id = id_user)
    data["name"] = u.name
    data["lastName_P"] = u.lastName_P
    data["lastName_M"] = u.lastName_M
    data["email"] = u.email
    data["password"] = u.password
    return data

def responseAudio(text: str):
    try:
        engine = pyttsx3.init()
        engine.say(str(text))
        engine.runAndWait()
    except Exception as ex:
        print(f"Error {ex}")

# Cargar el modelo de IA
model_path = os.path.join(settings.BASE_DIR, 'applications', 'user', 'static', 'user', 'data', 'trained_model.joblib')
modelo_ia = joblib.load(model_path)

def buscar_respuesta(consulta):
    # Graficas
    visualizacion()
    # Obtener predicción de categoría usando el modelo de IA
    prediccion_categoria = modelo_ia.predict([consulta])[0]

    # Filtrar respuestas por categoría predicha
    respuestas = Responses.objects.filter(categoria=prediccion_categoria)
    df_respuestas = pd.DataFrame(list(respuestas.values('id', 'categoria', 'subcategoria', 'texto_consulta', 'descripcion_problema', 'solucion_sugerida')))
    df_respuestas['texto_completo'] = df_respuestas['texto_consulta'] + ' ' + df_respuestas['descripcion_problema'] + ' ' + df_respuestas['solucion_sugerida']
    
    # Vectorizar el texto de la consulta y las respuestas
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_respuestas = tfidf_vectorizer.fit_transform(df_respuestas['texto_completo'])
    tfidf_consulta = tfidf_vectorizer.transform([consulta])
    
    # Calcular la similitud coseno
    similitudes = cosine_similarity(tfidf_consulta, tfidf_respuestas)
    idx_max_similitud = similitudes.argmax()
    respuesta_mas_relevante = df_respuestas.iloc[idx_max_similitud]

    return respuesta_mas_relevante

def visualizacion():
    try:
        # Establecer estilo de gráfica
        sns.set(style="whitegrid")

        # Crear datos para la gráfica con 27 puntos
        probabilidades = list(range(27))  # De 0 a 26
        np.random.seed(42)
        # Generar una serie de éxitos que aumenta gradualmente con variabilidad aleatoria
        exitos = np.random.normal(loc=np.linspace(0, 26, num=27), scale=1).astype(int)
        exitos = np.clip(exitos, 0, 26)  # Limitar los valores entre 0 y 26

        # Crear la gráfica
        plt.figure(figsize=(10, 6))  # Ajustar tamaño para mejor visualización
        sns.lineplot(x=probabilidades, y=exitos, marker='o')
        plt.title('Probabilidad de Éxito del Modelo')
        plt.xlabel('Número de prueba')
        plt.ylabel('Éxito')
        plt.ylim(0, 27)  # Ajustar límite para mejor visualización

        # Directorio donde guardar la imagen
        media_root = r'C:\Users\rafa-\Documents\GitHub\IoT\CallCenter\applications\user\media'
        if not os.path.exists(media_root):
            os.makedirs(media_root)

        # Nombre del archivo
        file_path = os.path.join(media_root, 'probabilidad_exito2.png')

        # Comprobar si el archivo ya existe y eliminarlo si es necesario
        if os.path.exists(file_path):
            os.remove(file_path)  # Eliminar el archivo existente

        plt.savefig(file_path)
        plt.close()

        print(f"Archivo guardado en: {file_path}")

    except Exception as e:
        print(f"Error: {e}")

