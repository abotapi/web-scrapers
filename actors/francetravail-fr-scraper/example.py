"""France Travail Scraper: minimal example. Docs: https://apify.com/abotapi/francetravail-fr-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/francetravail-fr-scraper").call(
    run_input={
        "mode": "search",
        "queries": ["developpeur"],
        "location": "Paris",
        "publishedDate": "Last Week",
        "contractType": ["Permanent contract (CDI) | CDI"],
        "contractDuration": ["Full-time | Temps plein"],
        "jobCategory": ["IT | Informatique, Télécommunication"],
        "sortBy": "Newest | Date",
        "maxItems": 10,
        "maxPages": 1,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
