"""Yellow Pages NZ Scraper: minimal example. Docs: https://apify.com/abotapi/yellow-nz-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/yellow-nz-scraper").call(
    run_input={
        "startUrls": [{"url": "https://yellow.co.nz/search?search_terms=Plumbers&geo_location_terms=Auckland"}, {"url": "https://yellow.co.nz/auckland/plumbers"}, {"url": "https://yellow.co.nz/auckland/bpp/onehunga-plumbers-579426046"}],
        "searchTerms": "Plumbers",
        "location": "New Zealand",
        "maxListings": 10,
        "maxPages": 1,
        "maxReviews": 10,
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
