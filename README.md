# `datos.gob.es` Data Catalog Export 🗃️

Automated scripts to create comprehensive snapshots of Spain's open government data ecosystem from the `datos.gob.es` catalog using [their JSON API](https://datos.gob.es/en/accessible-apidata).

## 🚀 Quick Start

```bash
# Install dependencies
make setup

# Fetch complete catalog data
make catalog

# Upload to Hugging Face (requires HUGGINGFACE_TOKEN)
make upload
```

## 📋 Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [HuggingFace](https://huggingface.co/) Token (for uploading datasets)

## 🛠️ Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd datosgobes-catalog
```

2. Install dependencies:
```bash
make setup
```

This will use `uv` to install all required Python packages from `pyproject.toml`.

## 📊 Available Commands

The [Makefile](./Makefile) provides convenient commands to fetch different types of data:

- `make apidata-docs` - Fetch and save API documentation
- `make datasets` - Export all datasets metadata
- `make publishers` - Export publisher information
- `make spatials` - Export geographical coverage data
- `make themes` - Export theme/category information
- `make public-sectors` - Export public sector taxonomy
- `make provinces` - Export province information
- `make catalog` - Run all exports (complete catalog snapshot)

## 📚 API Documentation

The datos.gob.es API documentation is automatically fetched and saved to [`apidata.md`](./apidata.md). This file contains:

- Available endpoints
- Response formats (JSON, XML, RDF, Turtle, CSV)
- Query parameters for filtering and pagination
- Examples of API usage

## 🗂️ Data Structure

Exported data is saved in the `catalog/` directory with the following structure:
```
catalog/
├── datasets/           # Dataset metadata
├── publishers/         # Publisher information
├── spatials/          # Geographical coverage
├── themes/            # Categories/topics
├── public-sectors/    # NTI public sector taxonomy
└── provinces/         # Province data
```

## 🚀 Uploading to Hugging Face

To upload the catalog to Hugging Face Hub:

```bash
export HUGGINGFACE_TOKEN=your_token_here
make upload
```

This uploads the entire `catalog/` directory to the `datania/datosgobes-catalog` dataset repository.

## 📄 License

MIT.
