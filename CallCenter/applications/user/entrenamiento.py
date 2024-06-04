import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

import os
from django.conf import settings

# Cargar el dataset preprocesado
file_path = os.path.join(settings.BASE_DIR, 'applications', 'user', 'static', 'user', 'data', 'Dataset_preprocessed.xlsx')
df = pd.read_excel(file_path)

# Combinar las columnas de texto para crear una entrada más completa
df['Texto Completo'] = df['Texto de la Consulta'] + ' ' + df['Descripción del Problema'] + ' ' + df['Solución Sugerida']

# Seleccionar las características y la etiqueta (puede ser la Categoría o Subcategoría)
X = df['Texto Completo']
y = df['Categoría']  # O df['Subcategoría'] si prefieres

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un pipeline con TF-IDF y Naive Bayes
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = pipeline.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Mostrar los resultados
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

# Guardar el modelo entrenado
import joblib
model_path = os.path.join(settings.BASE_DIR, 'applications', 'user', 'static', 'user', 'data', 'trained_model.jobliby')
joblib.dump(pipeline, model_path)

model_path
