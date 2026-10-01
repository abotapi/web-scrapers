# Zara Scraper

Scrape Zara (zara.com) products: current price plus strike-through Rebajas (sale) discount, full colour variant matrix with per-colour availability, and (with full detail) fabric composition and a per-size availability/price matrix. Browse by category or Rebajas, or paste links.

**[Open Zara Scraper on Apify](https://apify.com/abotapi/zara-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zara-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "es/es", "section": "WOMAN", "categoryId": "2420896", "sortBy": "relevance", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `market` | string | Market (country/language) |
| `section` | string | Section |
| `categoryId` | string | Category id |
| `specialsOnly` | boolean | Rebajas (sale) only |
| `urls` | array | URLs to scrape |
| `searchTerm` | string | Keyword filter |
| `colors` | array | Colours |
| `sizes` | array | Sizes |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch full product detail |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zara-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `reference` | string |
| `section` | string |
| `family` | string |
| `subfamily` | string |
| `kind` | string |
| `description` | string |
| `url` | string |
| `currency` | string |
| `defaultColorId` | string |
| `colors` | list |
| `compositions` | null |
| `reviews` | list |
| `price` | float |
| `oldPrice` | null |
| `originalPrice` | null |
| `discountPercent` | null |
| `isOnSale` | boolean |
| `availability` | string |
| `image` | string |

---

[← All scrapers](../../README.md)
