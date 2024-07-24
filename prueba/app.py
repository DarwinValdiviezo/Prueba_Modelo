import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import pickle
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('modelo_rna.h5')

# Cargar el scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Función para convertir entradas categóricas a variables dummy
def process_categorical_input(data):
    categorical_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'country']
    dummy_data = pd.get_dummies(pd.DataFrame([data]), columns=categorical_cols)
    # Asegurarse de que las columnas estén en el mismo orden que en el entrenamiento
    dummy_data = dummy_data.reindex(columns=scaler.feature_names_in_, fill_value=0)
    return dummy_data.values

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del formulario
    form_data = request.form.to_dict()
    
    # Verificar si algún campo está vacío
    for key, value in form_data.items():
        if value == '':
            return render_template('index.html', error_message='Por favor, llene todos los campos antes de enviar.')

    # Convertir valores numéricos a float y validar rangos
    numeric_cols = {
        'age': (18, 100),
        'fnlwgt': (1, float('inf')),
        'education-num': (1, 20),
        'capital-gain': (0, float('inf')),
        'capital-loss': (0, float('inf')),
        'hours-per-week': (1, 100)
    }
    for col, (min_val, max_val) in numeric_cols.items():
        try:
            form_data[col] = float(form_data[col])
            if not (min_val <= form_data[col] <= max_val):
                return render_template('index.html', error_message=f'El valor de {col} debe estar entre {min_val} y {max_val}.')
        except ValueError:
            return render_template('index.html', error_message=f'El campo {col} debe ser un número válido.')

    # Procesar entradas categóricas
    processed_data = process_categorical_input(form_data)
    
    # Escalar los datos
    scaled_features = scaler.transform(processed_data)
    
    # Realizar predicción
    prediction = model.predict(scaled_features)
    probability = prediction[0][0]
    
    return render_template(
        'index.html', 
        prediction_text=f'Predicción: {"Menos de 50K" if probability > 0.5 else "Más de 50K"}',
        probability_text=f'Probabilidad de >50K: {probability * 100:.2f}%, Probabilidad de <=50K: {(1 - probability) * 100:.2f}%',
        message='¡Sigue trabajando!'
    )

if __name__ == "__main__":
    app.run(debug=True)
