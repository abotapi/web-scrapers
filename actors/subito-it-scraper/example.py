"""Subito.it Scraper: minimal example. Docs: https://apify.com/abotapi/subito-it-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/subito-it-scraper").call(
    run_input={
        "category": "marketplace",
        "sellerType": "any",
        "sort": "datedesc",
        "adType": "s",
        "startUrls": [{"url": "https://www.subito.it/annunci-italia/vendita/usato/?q=bici"}, {"url": "https://www.subito.it/annunci-italia/vendita/usato/?q=bici&o=2"}, {"url": "https://www.subito.it/annunci-italia/vendita/usato/?q=bici&sort=priceasc&ps=10&pe=100"}, {"url": "https://www.subito.it/annunci-italia/vendita/usato/?q=bici&advt=1"}, {"url": "https://www.subito.it/annunci-italia/vendita/usato/?q=bici&shp=true"}, {"url": "https://www.subito.it/annunci-lombardia/vendita/usato/milano/?q=bici"}, {"url": "https://www.subito.it/annunci-italia/vendita/usato/"}, {"url": "https://www.subito.it/annunci-italia/vendita/biciclette/"}, {"url": "https://www.subito.it/annunci-lombardia/vendita/auto/"}, {"url": "https://www.subito.it/annunci-italia/vendita/auto/toyota/corolla/"}, {"url": "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/"}, {"url": "https://www.subito.it/annunci-italia/vendita/immobili/"}, {"url": "https://www.subito.it/annunci-italia/vendita/appartamenti/"}, {"url": "https://www.subito.it/annunci-lazio/affitto/appartamenti/roma/?ps=500&pe=1200"}, {"url": "https://www.subito.it/annunci-italia/affitto/appartamenti/"}, {"url": "https://www.subito.it/annunci-italia/vendita/offerte-lavoro/"}, {"url": "https://www.subito.it/annunci-italia/cerco/usato/?q=bici"}, {"url": "https://www.subito.it/annunci-italia/regalo/usato/"}, {"url": "https://www.subito.it/bambini-giocattoli/seggiolino-bici-con-morsetto-di-attacco-arezzo-665060654.htm"}, {"url": "https://www.subito.it/auto/mercedes-benz-b200-treviso-664945738.htm"}, {"url": "https://www.subito.it/utente/106698735"}, {"url": "https://m.subito.it/annunci-italia/vendita/usato/?q=bici"}],
        "maxItems": 10,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "IT"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
