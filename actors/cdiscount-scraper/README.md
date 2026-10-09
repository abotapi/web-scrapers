# Cdiscount Scraper

Scrape product data from Cdiscount.com by keyword, category, or URL. Apply filters and sorting, then enrich results with full product details, marketplace seller information, pricing, availability, specifications, ratings, and customer reviews.

**[Open Cdiscount Scraper on Apify](https://apify.com/abotapi/cdiscount-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~cdiscount-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchWord": "telephone", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "FR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchWord` | string | Search keyword |
| `departmentId` | string | Department / category ID (optional) |
| `filterIds` | array | Filter IDs (advanced, optional) |
| `sortBy` | string | Sort by |
| `urls` | array | Start URLs |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/cdiscount-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `productId` | string |
| `offerId` | integer |
| `name` | string |
| `brand` | null |
| `url` | string |
| `categoryPath` | string |
| `condition` | string |
| `price` | float |
| `currency` | string |
| `priceWithoutVAT` | float |
| `originalPrice` | float |
| `discountPercent` | integer |
| `discountAmount` | integer |
| `promoLabel` | null |
| `isAvailable` | boolean |
| `sponsored` | boolean |
| `freeShipping` | string |
| `media` | list |
| `previewImage` | string |
| `rating` | null |
| `reviewCount` | null |
| `characteristics` | object |
| `sellerId` | integer |
| `sellerName` | string |
| `sellerRating` | float |
| `sellerRatingsCount` | integer |
| `sellerSalesCount` | integer |
| `sellerCountry` | string |
| `sellerRaw` | object |
| `hasDetail` | boolean |
| `sourceMode` | string |
| `searchWord` | string |

---

[← All scrapers](../../README.md)
