"""THE ICONIC Scraper: minimal example. Docs: https://apify.com/abotapi/theiconic-com-au-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/theiconic-com-au-scraper").call(
    run_input={
        "mode": "search",
        "searchTerms": ["t-shirt"],
        "sortBy": "popularity",
        "maxReviews": 10,
        "maxPages": 1,
        "maxItems": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
        "changeScope": "all",
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
