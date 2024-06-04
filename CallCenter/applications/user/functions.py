from .models import *
import pyttsx3
from applications.user.models import *

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import joblib
import os
from django.conf import settings

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

    # print("Categoría:", respuesta_mas_relevante['categoria'])
    # print("Subcategoría:", respuesta_mas_relevante['subcategoria'])
    # print("Consulta:", respuesta_mas_relevante['texto_consulta'])
    # print("Descripción del Problema:", respuesta_mas_relevante['descripcion_problema'])
    # print("Solución Sugerida:", respuesta_mas_relevante['solucion_sugerida'])
    
    return respuesta_mas_relevante

