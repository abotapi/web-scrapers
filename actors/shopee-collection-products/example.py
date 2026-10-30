"""Shopee Cambodia Scraper: minimal example. Docs: https://apify.com/abotapi/shopee-collection-products

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/shopee-collection-products").call(
    run_input={
        "urls": ["https://shopeekh.com/collections/12453606", "https://shopeekh.com/collections/12453606?page=1", "https://shopeekh.com/m/Shopee-Beauty", "https://shopeekh.com/api/v4/microsite/get_products_for_collection_landing_page?by=relevancy&card_set_name=Microsite%20ATC%20Card&collection_id=12453606&item_order=0&limit=60&match_id=12453606&need_customised_item_card=True&newest=0&offset=0&order=desc", "https://shopeekh.com/api/v4/pagebuilder/get_csr_page?page_url=Shopee-Beauty&platform=4&timestamp=0"],
        "maxItems": 10,
        "maxPages": 1,
        "sortBy": "relevance",
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
