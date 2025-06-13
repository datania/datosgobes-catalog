import asyncio
import json
import re
import time
from pathlib import Path
from typing import Optional

import httpx

BASE_URL = "https://datos.gob.es/apidata/nti/public-sector"
PAGE_SIZE = 50
CONCURRENT_PAGES = 20
MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 1.0


async def fetch_page(client: httpx.AsyncClient, page: int) -> Optional[dict]:
    """Fetch a single page of public sector listings with retry and exponential backoff"""
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
                
            delay = INITIAL_RETRY_DELAY * (2 ** attempt)
            print(f"Retry {attempt + 1}/{MAX_RETRIES} for page {page} in {delay:.1f}s: {e}")
            await asyncio.sleep(delay)


def sanitize_slug(url: str) -> str:
    """Extract and sanitize slug from _about URL"""
    if not url:
        return ""
    
    # Extract the last part of the URL path
    slug = url.split("/")[-1] if url else ""
    
    # Replace spaces and special characters with hyphens
    sanitized = re.sub(r'[^\w\-]', '-', slug)
    # Remove multiple consecutive hyphens
    sanitized = re.sub(r'-+', '-', sanitized)
    # Remove leading/trailing hyphens
    sanitized = sanitized.strip('-')
    return sanitized.lower()


def extract_public_sector_id(item: dict) -> str:
    """Extract public sector ID from the _about URL"""
    url = item.get("_about", "")
    return sanitize_slug(url)


def get_public_sector_path(sector_id: str) -> Path:
    """Generate path for a public sector JSON file"""
    if not sector_id:
        return Path("catalog/public-sector/misc/unknown.json")
    
    filename = f"{sector_id}.json"
    return Path("catalog/public-sector") / filename


async def export_all_public_sectors():
    """Export all public sectors from datos.gob.es to local JSON files"""
    print("Starting public sector export...")
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

            # Process all public sectors from fetched pages
            found_any = False
            sectors_to_save = []

            for page_data in page_results:
                if page_data and page_data.get("result", {}).get("items"):
                    found_any = True
                    items = page_data["result"]["items"]
                    total_found += len(items)

                    for item in items:
                        sector_id = extract_public_sector_id(item)
                        if sector_id:
                            sectors_to_save.append((sector_id, item))

            empty_pages = 0 if found_any else empty_pages + 1

            # Save public sectors
            for sector_id, data in sectors_to_save:
                try:
                    file_path = get_public_sector_path(sector_id)
                    file_path.parent.mkdir(parents=True, exist_ok=True)

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)

                    total_saved += 1
                except Exception as e:
                    print(f"Error saving public sector {sector_id}: {e}")

            # Progress update
            if sectors_to_save:
                elapsed = time.time() - start_time
                rate = total_saved / elapsed if elapsed > 0 else 0
                print(
                    f"Pages {page}-{page + CONCURRENT_PAGES - 1}: "
                    f"Saved {total_saved}/{total_found} public sectors ({rate:.1f}/sec)"
                )

            page += CONCURRENT_PAGES

    # Final summary
    elapsed = time.time() - start_time
    print("\nExport complete!")
    print(f"Total public sectors: {total_found}")
    print(f"Successfully saved: {total_saved}")
    print(f"Failed: {total_found - total_saved}")
    print(f"Time: {elapsed:.1f} seconds ({total_saved / elapsed:.1f} public sectors/sec)")
    print(f"Location: {Path('catalog/public-sector').absolute()}/")


if __name__ == "__main__":
    asyncio.run(export_all_public_sectors())