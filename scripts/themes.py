import asyncio
import json
import time
from pathlib import Path
from typing import Optional

import httpx

BASE_URL = "https://datos.gob.es/apidata/catalog/theme"
PAGE_SIZE = 50
CONCURRENT_PAGES = 20
MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 1.0


async def fetch_page(client: httpx.AsyncClient, page: int) -> Optional[dict]:
    """Fetch a single page of theme listings with retry and exponential backoff"""
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


def extract_theme_id(item: dict) -> str:
    """Extract theme ID from notation field"""
    return item.get("notation", "")


def get_theme_path(theme_id: str) -> Path:
    """Generate path for a theme JSON file"""
    if not theme_id:
        return Path("catalog/theme/misc/unknown.json")
    
    filename = f"{theme_id}.json"
    return Path("catalog/theme") / filename


async def export_all_themes():
    """Export all themes from datos.gob.es to local JSON files"""
    print("Starting theme export...")
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

            # Process all themes from fetched pages
            found_any = False
            themes_to_save = []

            for page_data in page_results:
                if page_data and page_data.get("result", {}).get("items"):
                    found_any = True
                    items = page_data["result"]["items"]
                    total_found += len(items)

                    for item in items:
                        theme_id = extract_theme_id(item)
                        if theme_id:
                            themes_to_save.append((theme_id, item))

            empty_pages = 0 if found_any else empty_pages + 1

            # Save themes
            for theme_id, data in themes_to_save:
                try:
                    file_path = get_theme_path(theme_id)
                    file_path.parent.mkdir(parents=True, exist_ok=True)

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)

                    total_saved += 1
                except Exception as e:
                    print(f"Error saving theme {theme_id}: {e}")

            # Progress update
            if themes_to_save:
                elapsed = time.time() - start_time
                rate = total_saved / elapsed if elapsed > 0 else 0
                print(
                    f"Pages {page}-{page + CONCURRENT_PAGES - 1}: "
                    f"Saved {total_saved}/{total_found} themes ({rate:.1f}/sec)"
                )

            page += CONCURRENT_PAGES

    # Final summary
    elapsed = time.time() - start_time
    print("\nExport complete!")
    print(f"Total themes: {total_found}")
    print(f"Successfully saved: {total_saved}")
    print(f"Failed: {total_found - total_saved}")
    print(f"Time: {elapsed:.1f} seconds ({total_saved / elapsed:.1f} themes/sec)")
    print(f"Location: {Path('catalog/theme').absolute()}/")


if __name__ == "__main__":
    asyncio.run(export_all_themes())