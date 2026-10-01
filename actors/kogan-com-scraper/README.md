# Kogan.com Scraper

Scrape Kogan.com products with full details and customer reviews. Search by keyword or paste category/search URLs across the AU, NZ and US stores. Returns price, stock, brand, GTIN, images, ratings, and review text.

**[Open Kogan.com Scraper on Apify](https://apify.com/abotapi/kogan-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kogan-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["headphones"], "store": "au", "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `store` | string | Store region |
| `brand` | string | Brand |
| `sortBy` | string | Sort by |
| `specialsCategory` | string | Specials category |
| `urls` | array | Kogan URLs |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kogan-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `store` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `sku` | string |
| `gtin` | string |
| `price` | integer |
| `priceMax` | null |
| `originalPrice` | null |
| `originalPriceLabel` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `specialsCategory` | null |
| `currency` | string |
| `availability` | string |
| `category` | string |
| `condition` | string |
| `description` | string |
| `image` | string |
| `images` | list |
| `averageRating` | float |
| `ratingCount` | integer |
| `productId` | string |
| `position` | integer |
| `searchMode` | string |

---

[← All scrapers](../../README.md)
