# Zalando Scraper

Scrape Zalando products: name, brand, current and original price, discount, sizes, images, deal flags and rating, plus full description, colour, per-size availability and reviews on detail. Search by keyword with sort and filters, or paste any category, search or product URL.

**[Open Zalando Scraper on Apify](https://apify.com/abotapi/zalando-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zalando-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["dress"], "domain": "co.uk", "specialsCategory": "none", "sortBy": "relevance", "maxReviews": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `domain` | string | Zalando country site |
| `specialsCategory` | string | Browse sale |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `onSaleOnly` | boolean | On sale only |
| `urls` | array | Category, search or product URLs |
| `fetchDetails` | boolean | Fetch full product details |
| `maxReviews` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zalando-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `targetGroup` | string |
| `category` | string |
| `supplierName` | string |
| `shortDescription` | null |
| `condition` | null |
| `price` | float |
| `originalPrice` | float |
| `promotionalPrice` | null |
| `discountPercentage` | null |
| `currency` | string |
| `onSale` | boolean |
| `dealFlag` | null |
| `flags` | list |
| `sizes` | list |
| `sizeSkus` | list |
| `image` | string |
| `images` | list |
| `rating` | null |
| `available` | boolean |
| `variantCount` | integer |
| `inWishlist` | boolean |
| `benefits` | list |
| `priceTrackingKey` | string |
| `domain` | string |
| `search_query` | string |
| `sourceUrl` | string |
| `productsFound` | integer |
| `mode` | string |
| `item` | object |
| `title` | string |
| `wasPrice` | null |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `isOnSpecial` | boolean |
| `promoLabel` | null |
| `specialsCategory` | null |

---

[← All scrapers](../../README.md)
