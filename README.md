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