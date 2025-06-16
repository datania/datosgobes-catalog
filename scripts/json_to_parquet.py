import json
from pathlib import Path

import polars as pl


def main():
    catalog_dir = Path(__file__).parent.parent / "catalog"
    dataset_dir = catalog_dir / "dataset"

    # Read all JSON files
    data = []
    for json_file in dataset_dir.rglob("*.json"):
        with open(json_file) as f:
            record = json.load(f)

        # Convert nested fields to strings
        for k, v in record.items():
            if isinstance(v, (dict, list)):
                record[k] = json.dumps(v, ensure_ascii=False)

        # Add metadata
        record["file_path"] = str(json_file.relative_to(catalog_dir))
        record["publisher_id"] = json_file.parent.parent.name

        data.append(record)

    # Create DataFrame and save
    df = pl.DataFrame(data)
    df.write_parquet(dataset_dir / "datasets.parquet", compression="zstd")

    print(f"Saved {len(df)} records to datasets.parquet")


if __name__ == "__main__":
    main()
