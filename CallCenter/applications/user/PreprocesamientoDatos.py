import pandas as pd
import re
import os
from django.conf import settings

# Cargar el dataset
file_path = os.path.join(settings.BASE_DIR, 'applications', 'user', 'static', 'user', 'data', 'Dataset.xlsx')
print(f"Hola: {file_path}")
df = pd.read_excel(file_path)

# Función de preprocesamiento
def preprocess_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar caracteres especiales y números
    text = re.sub(r'[^a-záéíóúñü\s]', '', text)
    # Tokenizar el texto (simulación básica)
    tokens = text.split()
    # Unir tokens en una sola cadena
    text = ' '.join(tokens)
    return text

# Aplicar el preprocesamiento a las columnas relevantes
df['Texto de la Consulta'] = df['Texto de la Consulta'].apply(preprocess_text)
df['Descripción del Problema'] = df['Descripción del Problema'].apply(preprocess_text)
df['Solución Sugerida'] = df['Solución Sugerida'].apply(preprocess_text)

# Guardar el dataset preprocesado
output_path = os.path.join(settings.BASE_DIR, 'applications', 'user', 'static', 'user', 'data', 'Dataset_preprocessed.xlsx')
df.to_excel(output_path, index=False)

output_path
