# Falabella Scraper

Scrape Falabella, Latin America's leading retail marketplace: products with local prices, discounts, ratings and seller info across the Chile, Colombia and Peru storefronts. Search keywords or paste links, and monitor price changes with recurring updates.

**[Open Falabella Scraper on Apify](https://apify.com/abotapi/falabella-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~falabella-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "cl", "queries": ["iphone"], "sort": "relevance", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `market` | string | Market |
| `queries` | array | Search terms |
| `sort` | string | Ordering |
| `urls` | array | Product or listing links |
| `fetchDetails` | boolean | Read product detail pages |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per source |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/falabella-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `skuId` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `imageUrl` | string |
| `currency` | string |
| `price` | integer |
| `priceDisplay` | string |
| `oldPrice` | null |
| `discountPercent` | null |
| `ratingAverage` | integer |
| `ratingCount` | integer |
| `sellerId` | string |
| `sellerName` | string |
| `officialSeller` | boolean |
| `sponsored` | boolean |
| `bestSeller` | boolean |
| `installments` | list |
| `shippingOptions` | list |
| `market` | string |
| `marketHost` | string |
| `sourceType` | string |
| `sourceId` | string |
| `sourceUrl` | null |
| `position` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
