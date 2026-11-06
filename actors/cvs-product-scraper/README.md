# CVS Scraper

Scrape CVS.com pharmacy, beauty, health and personal care products by keyword search. Extract product names, brands, prices, descriptions, ratings, customer reviews and availability. Collect structured product data for price comparison, competitor analysis, market research and stock monitoring.

**[Open CVS Scraper on Apify](https://apify.com/abotapi/cvs-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~cvs-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "urls", "searchTerms": ["shampoo"], "urls": [{"url": "https://www.cvs.com/shop/l-a-girl-shimmer-spray-gold-prodid-186492"}, {"url": "https://www.cvs.com/search?q=shampoo"}], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Storefront links |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/cvs-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `skuId` | null |
| `url` | string |
| `title` | string |
| `brand` | string |
| `price` | float |
| `wasPrice` | null |
| `pricePerUnit` | null |
| `currency` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `rating` | float |
| `reviewsCount` | integer |
| `sponsored` | null |
| `badges` | list |
| `position` | null |
| `description` | string |
| `availability` | string |
| `reviewsAverage` | null |
| `reviewsRecommended` | null |
| `ratingDistribution` | list |
| `reviews` | list |
| `reviewsTotal` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
