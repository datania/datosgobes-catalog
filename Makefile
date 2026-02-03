.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

setup: .uv
	uv sync

apidata-docs:
	@curl -s "https://r.jina.ai/datos.gob.es/en/accessible-apidata" > apidata.md

datasets:
	uv run scripts/datasets.py

publishers:
	uv run scripts/publishers.py

spatials:
	uv run scripts/spatials.py

themes:
	uv run scripts/themes.py

public-sectors:
	uv run scripts/public-sectors.py

provinces:
	uv run scripts/provinces.py

catalog: apidata-docs datasets publishers spatials themes public-sectors provinces

parquets:
	uv run scripts/json_to_parquet.py catalog/dataset datasets
	uv run scripts/json_to_parquet.py catalog/publisher publishers
	uv run scripts/json_to_parquet.py catalog/province provinces
	uv run scripts/json_to_parquet.py catalog/spatial spatial
	uv run scripts/json_to_parquet.py catalog/theme themes
	uv run scripts/json_to_parquet.py catalog/public-sector public-sectors

upload:
	HF_HUB_ENABLE_HF_TRANSFER=1 \
	uvx --from "huggingface_hub[hf_xet]" hf upload-large-folder \
		--token=${HUGGINGFACE_TOKEN} \
		--repo-type dataset \
		--num-workers 4 \
		--no-bars \
		datania/datosgobes-catalog catalog/
