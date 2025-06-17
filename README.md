# Catálogo de Datos de `datos.gob.es` 🗃️

Herramientas para exportar el catálogo de `datos.gob.es` de forma periódica usando la [API JSON](https://datos.gob.es/es/accessible-apidata).

## 🚀 Inicio

```bash
# Instalar dependencias
make setup

# Obtener datos completos del catálogo
make catalog

# Subir a Hugging Face (requiere HUGGINGFACE_TOKEN)
make upload
```

## 📋 Prerrequisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Token de [HuggingFace](https://huggingface.co/) (para subir conjuntos de datos)

## 🛠️ Configuración

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd datosgobes-catalog
```

2. Instalar dependencias:
```bash
make setup
```

Esto usará `uv` para instalar todos los paquetes especificados en el archivo `pyproject.toml`.

## 📊 Comandos Disponibles

El [Makefile](./Makefile) proporciona comandos útiles para obtener diferentes tipos de datos:

- `make apidata-docs` - Obtener y guardar la documentación de la API
- `make datasets` - Exportar todos los metadatos de conjuntos de datos
- `make publishers` - Exportar información de publicadores
- `make spatials` - Exportar datos de cobertura geográfica
- `make themes` - Exportar información de temas/categorías
- `make public-sectors` - Exportar taxonomía del sector público
- `make provinces` - Exportar información de provincias
- `make catalog` - Ejecutar todas las exportaciones (instantánea completa del catálogo)

## 📚 Documentación de la API

La documentación de la API de `datos.gob.es` se actualiza automáticamente y se guarda en [`apidata.md`](./apidata.md). Este archivo contiene:

- Endpoints disponibles
- Formatos de respuesta (JSON, XML, RDF, Turtle, CSV)
- Parámetros de consulta para filtrado y paginación
- Ejemplos de uso de la API

## 🗂️ Estructura de Datos

Los datos exportados se guardan en el directorio `catalog/` con la siguiente estructura:
```
catalog/
├── datasets/           # Metadatos de conjuntos de datos
├── publishers/         # Información de publicadores
├── spatials/          # Cobertura geográfica
├── themes/            # Categorías/temas
├── public-sectors/    # Taxonomía NTI del sector público
└── provinces/         # Datos de provincias
```

## 🚀 Subir a Hugging Face

Para subir el catálogo a Hugging Face Hub:

```bash
export HUGGINGFACE_TOKEN=tu_token_aquí
make upload
```

Esto sube todo el directorio `catalog/` al repositorio de conjunto de datos `datania/datosgobes-catalog`.

## 📄 Licencia

MIT.
