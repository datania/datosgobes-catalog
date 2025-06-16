import argparse
import json
from pathlib import Path

import polars as pl


def main():
    parser = argparse.ArgumentParser(
        description="Convert JSON files in a folder to a Parquet file"
    )
    parser.add_argument("folder", help="Path to the folder containing JSON files")
    parser.add_argument("output_name", help="Name of the output Parquet file (without .parquet extension)")
    args = parser.parse_args()

    folder_path = Path(args.folder)
    if not folder_path.exists():
        print(f"Error: Folder {folder_path} does not exist")
        return

    catalog_dir = Path(__file__).parent.parent / "catalog"
    
    # Read all JSON files
    data = []
    for json_file in folder_path.rglob("*.json"):
        with open(json_file) as f:
            record = json.load(f)

        # Convert nested fields to strings
        for k, v in record.items():
            if isinstance(v, (dict, list)):
                record[k] = json.dumps(v, ensure_ascii=False)

        # Add metadata
        try:
            record["file_path"] = str(json_file.relative_to(catalog_dir))
        except ValueError:
            # If the file is not under catalog_dir, use relative to folder_path
            record["file_path"] = str(json_file.relative_to(folder_path))
        
        # For dataset folder, extract publisher_id from path structure
        if "dataset" in folder_path.parts:
            if json_file.parent.parent.name != folder_path.name:
                record["publisher_id"] = json_file.parent.parent.name

        data.append(record)

    if not data:
        print(f"No JSON files found in {folder_path}")
        return

    # Create DataFrame and save
    df = pl.DataFrame(data)
    output_file = folder_path / f"{args.output_name}.parquet"
    df.write_parquet(output_file, compression="zstd")

    print(f"Saved {len(df)} records to {output_file}")


if __name__ == "__main__":
    main()
