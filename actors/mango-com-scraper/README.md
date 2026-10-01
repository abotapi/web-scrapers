# Mango Scraper

Scrape Mango (shop.mango.com) fashion products: current price plus strike-through Rebajas (sale) discount, full colour/size variant matrix, section and category, and (with full detail) composition, care, materials, origin, fit and per-size availability. Search by keyword or Rebajas, or paste links.

**[Open Mango Scraper on Apify](https://apify.com/abotapi/mango-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mango-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "es/es", "section": "WOMEN", "searchTerm": "vestido", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `market` | string | Market (country/language) |
| `section` | string | Section |
| `searchTerm` | string | Search keyword |
| `specialsOnly` | boolean | Rebajas (sale) only |
| `urls` | array | URLs to scrape |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `fetchDetails` | boolean | Fetch full product detail |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mango-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `section` | string |
| `collection` | string |
| `model` | string |
| `category` | string |
| `families` | list |
| `url` | string |
| `defaultColorId` | string |
| `colors` | list |
| `reviews` | object |
| `price` | float |
| `currency` | string |
| `originalPrice` | float |
| `discountAmount` | integer |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `promoLabel` | string |
| `image` | string |

---

[← All scrapers](../../README.md)
