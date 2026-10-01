"""Letterboxd Scraper: minimal example. Docs: https://apify.com/abotapi/letterboxd-film-reviews-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/letterboxd-film-reviews-scraper").call(
    run_input={
        "mode": "search",
        "queries": ["dune"],
        "browsePath": "/films/popular/",
        "maxItems": 10,
        "maxPages": 1,
        "maxReviewsPerFilm": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["BUYPROXIES94952"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
