"""LTK Scraper: minimal example. Docs: https://apify.com/abotapi/shopltk-com-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/shopltk-com-scraper").call(
    run_input={
        "mode": "urls",
        "urls": ["https://www.shopltk.com/explore/amberfillerup", "https://liketk.it/5XXza", "https://www.shopltk.com/explore/chrisellelim/posts/35cf770f-19a8-11f1-b2f3-0242ac11001a", "https://www.shopltk.com/explore/chrisellelim/collections/11f0820026ce9c87be560242ac110021", "https://www.shopltk.com/categories/salealert", "https://www.shopltk.com/categories/findsunder100", "https://www.shopltk.com/categories/findsunder50", "/search?keyword=summer+dress"],
        "searchQueries": ["summer dress"],
        "maxItems": 10,
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
