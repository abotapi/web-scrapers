"""Vivino Wine Scraper: minimal example. Docs: https://apify.com/abotapi/vivino-wine-data-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/vivino-wine-data-scraper").call(
    run_input={
        "mode": "lookup",
        "wines": ["Dom Pérignon", "Opus One 2019", "https://www.vivino.com/cloudy-bay-sauvignon-blanc/w/18978"],
        "searchMode": "auto",
        "matchingMode": "basic",
        "sortBy": "relevance",
        "countryCode": "FR",
        "currencyCode": "EUR",
        "maxReviewsPerWine": 10,
        "maxItems": 10,
        "maxPages": 1,
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
