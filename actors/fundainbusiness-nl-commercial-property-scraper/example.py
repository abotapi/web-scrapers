"""Funda in Business Scraper: minimal example. Docs: https://apify.com/abotapi/fundainbusiness-nl-commercial-property-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/fundainbusiness-nl-commercial-property-scraper").call(
    run_input={
        "mode": "search",
        "locations": ["Amsterdam"],
        "propertyType": "all",
        "dealType": "both",
        "rentPriceBasis": "per_month",
        "publicationDate": "any",
        "parking": "any",
        "constructionType": "any",
        "auctionDate": "any",
        "openDay": "any",
        "sortBy": "relevance",
        "language": "nl",
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
