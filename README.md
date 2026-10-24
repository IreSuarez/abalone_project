# Projecto Abalone

Objetivo: predecir edad del molusco Abalón

## Entorno de desarrollo
- **Python:** 3.12
- **Gestor:** conda

## Pasos de Instalación
1) Clonar repositorio
2) Crear entorno: `conda create --name abalone_env python=3.12`
3) Activar entorno: `conda activate abalone_env`
4) Instalar dependencias: `pip install -r requirements.txt`

## Estructura del proyecto
- `data/`: Datos crudos y procesados.
- `src/`: Código fuente para preprocesamiento y modelado.
- `results/`: Métricas y registro de experimentos.
- `models/`: Modelos entrenados serializados.

## Ejecución del Preprocesamiento

Para limpiar los datos originales, sigue estos pasos:

1) Abre tu terminal.
2) Asegúrate de tener activado el entorno virtual (ejecutando `conda activate abalone_env`).
3) Verifica que estás posicionado en la carpeta principal del proyecto (`abalone_project`).
4) Ejecuta el script de preprocesamiento ingresando este comando y presionando Enter:
   `python src/preprocess.py`

## Ejecución del Entrenamiento

Para entrenar el modelo, sigue estos pasos:

1) Abre tu terminal
2) Asegúrate de tener activado el entorno virtual (ejecutando `conda activate abalone_env`).
3) Verifica que estás posicionado en la carpeta principal del proyecto (`abalone_project`).
4) Ejecuta el script del preprocesamiento ingresando este comando y presionando Eter: `python src/preprocess.py`



## Resultados Modelos
**V1:**

El Random Forest con max_depth=10 tiene un desempeño similar al de max_depth=None que se probó (model_v1) con:

MAE: 1.2155

RMSE: 1.6161

R2: 0.5309

**V2:**

El Random Forest con max_depth=15 tiene un desempeño similar al de max_depth=None que se probó (model_v1) con:

MAE: 1.2171

RMSE: 1.6195

R2: 0.5289

**V3:**

El Random Forest con max_depth=10 tiene un desempeño similar al de max_depth=None que se probó (model_v1) con:

MAE: 1.1972

RMSE: 1.6008

R2: 0.5397