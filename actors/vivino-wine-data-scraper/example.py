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
        "wines": ["Dom Pérignon", "Opus One 2019", "https://www.vivino.com/cloudy-bay-sauvignon-blanc/w/18978", "https://www.vivino.com/cloudy-bay-sauvignon-blanc/w/18978?year=2015", "https://www.vivino.com/FR/en/henschke-hill-of-grace/w/13563", "https://www.vivino.com/w/88177", "https://www.vivino.com/search/wines?q=chablis", "https://www.vivino.com/explore?country_code=FR&min_rating=4&wine_type_ids[]=1", "https://www.vivino.com/grapes/sauvignon-blanc", "https://www.vivino.com/wine-regions/marlborough", "https://www.vivino.com/wineries/cloudy-bay", "https://www.vivino.com/api/explore/explore?country_code=FR&currency_code=EUR&min_rating=4&page=1&order_by=ratings_average&order=desc", "https://www.vivino.com/api/wines/83919/reviews?per_page=2"],
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
