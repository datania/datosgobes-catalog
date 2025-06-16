import asyncio
import json
import time
from pathlib import Path
from typing import Optional

import httpx

BASE_URL = "https://datos.gob.es/apidata/catalog/dataset"
PAGE_SIZE = 50  # Maximum page size allowed by API
CONCURRENT_PAGES = 20  # More aggressive parallelization
MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 1.0  # seconds


async def fetch_page(client: httpx.AsyncClient, page: int) -> Optional[dict]:
    """Fetch a single page of dataset listings with retry and exponential backoff"""
    for attempt in range(MAX_RETRIES):
        try:
            response = await client.get(
                f"{BASE_URL}.json?_pageSize={PAGE_SIZE}&_page={page}"
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                print(f"Error fetching page {page} after {MAX_RETRIES} attempts: {e}")
                return None

            delay = INITIAL_RETRY_DELAY * (2**attempt)
            print(
                f"Retry {attempt + 1}/{MAX_RETRIES} for page {page} in {delay:.1f}s: {e}"
            )
            await asyncio.sleep(delay)


def extract_dataset_id(item: dict) -> str:
    """Extract dataset ID from the _about URL"""
    url = item.get("_about", "")
    return url.split("/")[-1] if url else ""


def get_dataset_path(dataset_id: str) -> Path:
    """
    Generate hierarchical path for a dataset using only the initial UUID part.
    """
    import hashlib

    # Extract just the first part before the hyphen (the UUID/identifier)
    uuid_part = dataset_id.split("-")[0] if "-" in dataset_id else dataset_id

    # Extract the remaining part after the UUID
    if "-" in dataset_id:
        remaining_part = dataset_id[len(uuid_part) + 1 :]  # +1 to skip the hyphen
        filename = f"{remaining_part}.json" if remaining_part else f"{uuid_part}.json"
    else:
        filename = f"{dataset_id}.json"

    # More aggressive filename shortening (under 100 chars for safety)
    max_name_length = 95  # Leave room for .json
    if len(filename) > max_name_length:
        name_without_ext = filename[:-5]  # Remove .json
        if len(name_without_ext) > max_name_length - 5:
            # Take first 60 chars and last 30 chars with hash for uniqueness
            hash_suffix = hashlib.md5(name_without_ext.encode()).hexdigest()[:8]
            truncated = name_without_ext[:60] + "-" + hash_suffix
            filename = truncated + ".json"

    if len(uuid_part) < 4:
        return Path("catalog/dataset/misc") / filename

    # Add subdirectory based on hash of full dataset_id to distribute files
    # Use modulo 1000 to create buckets from 000 to 999
    bucket = int(hashlib.md5(dataset_id.encode()).hexdigest()[:8], 16) % 1000
    bucket_dir = f"{bucket:03d}"  # Format as 3-digit string with leading zeros

    return Path(f"catalog/dataset/{uuid_part}/{bucket_dir}/{filename}")


async def export_all_datasets():
    """Export all datasets from datos.gob.es to local JSON files"""
    print("Starting dataset export...")
    start_time = time.time()

    async with httpx.AsyncClient(follow_redirects=True, timeout=30.0) as client:
        page = 0
        total_found = 0
        total_saved = 0
        empty_pages = 0

        # Process pages until we find 3 consecutive empty pages
        while empty_pages < 3:
            # Fetch multiple pages concurrently
            tasks = [fetch_page(client, page + i) for i in range(CONCURRENT_PAGES)]
            page_results = await asyncio.gather(*tasks)

            # Process all datasets from fetched pages
            found_any = False
            datasets_to_save = []

            for page_data in page_results:
                if page_data and page_data.get("result", {}).get("items"):
                    found_any = True
                    items = page_data["result"]["items"]
                    total_found += len(items)

                    for item in items:
                        dataset_id = extract_dataset_id(item)
                        if dataset_id:
                            datasets_to_save.append((dataset_id, item))

            empty_pages = 0 if found_any else empty_pages + 1

            # Save datasets directly (no additional API calls needed)
            for dataset_id, data in datasets_to_save:
                try:
                    file_path = get_dataset_path(dataset_id)
                    file_path.parent.mkdir(parents=True, exist_ok=True)

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)

                    total_saved += 1
                except Exception as e:
                    print(f"Error saving dataset {dataset_id}: {e}")

            # Progress update
            if datasets_to_save:
                elapsed = time.time() - start_time
                rate = total_saved / elapsed if elapsed > 0 else 0
                print(
                    f"Pages {page}-{page + CONCURRENT_PAGES - 1}: "
                    f"Saved {total_saved}/{total_found} datasets ({rate:.1f}/sec)"
                )

            page += CONCURRENT_PAGES

    # Final summary
    elapsed = time.time() - start_time
    print("\nExport complete!")
    print(f"Total datasets: {total_found}")
    print(f"Successfully saved: {total_saved}")
    print(f"Failed: {total_found - total_saved}")
    print(f"Time: {elapsed:.1f} seconds ({total_saved / elapsed:.1f} datasets/sec)")
    print(f"Location: {Path('catalog/dataset').absolute()}/")


if __name__ == "__main__":
    asyncio.run(export_all_datasets())
