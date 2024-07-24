# Predicción de Salario

Este proyecto implementa varios modelos de aprendizaje automático para predecir si el salario de una persona es mayor o menor a $50K al año. Utiliza Flask para crear una interfaz web que permite al usuario ingresar datos y obtener predicciones.

## Requisitos

1. Python 3.x
2. pip (gestor de paquetes de Python)
3. Git (opcional, para clonar el repositorio)

## Instalación

### Clonar el Repositorio

Puedes clonar el repositorio utilizando Git o descargar el código como un archivo ZIP.

```bash
git clone https://github.com/DarwinValdiviezo/Prueba_Modelo.git
cd Prueba_Modelo
```

## Crear y Activar un Entorno Virtual

Es una buena práctica utilizar un entorno virtual para gestionar las dependencias del proyecto.

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## Instalar Dependencias

Instala las dependencias necesarias utilizando pip:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

El proyecto debe tener la siguiente estructura:

```bash
.
├── app.py
├── modelo_rna.h5
├── scaler.pkl
├── data_evaluacion.csv
├── templates
│   └── index.html
├── static
│   └── styles.css
└── README.md
```

_app.py:_ Archivo principal que contiene la aplicación Flask.
_modelo_rna.h5:_ Archivo del modelo de red neuronal entrenado.
_scaler.pkl:_ Archivo del escalador entrenado.
_data_evaluacion.csv:_ Archivo CSV con los datos de evaluación.
_templates/index.html:_ Archivo HTML para la interfaz web.
_static/styles.css:_ Archivo CSS para estilos personalizados.
_README.md:_ Instrucciones y documentación del proyecto.

## Ejecución de la Aplicación

Para ejecutar la aplicación, simplemente ejecuta el archivo app.py:

```bash
python app.py
```

La aplicación estará disponible en http://127.0.0.1:5000/ en tu navegador web.

## Uso

1. Abre tu navegador web y ve a http://127.0.0.1:5000/.
2. Ingresa los datos requeridos en el formulario.
3. Haz clic en el botón "Predecir" para obtener la predicción del salario.
4. Para realizar una nueva predicción, haz clic en el botón "Nueva Predicción".

## Validación de Entradas

1. Todos los campos son obligatorios.
2. Los campos numéricos deben contener valores válidos dentro de los rangos especificados.
