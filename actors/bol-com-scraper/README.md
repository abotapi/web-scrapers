# bol.com Scraper

Scrape bol.com products: title, price, list price and discount, EAN, brand, images, condition, delivery, full specifications, ratings with distribution, individual reviews, every offer with seller name and rating, and refurbished prices. Search by keyword with filters, or paste product URLs.

**[Open bol.com Scraper on Apify](https://apify.com/abotapi/bol-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bol-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["laptop"], "sortBy": "relevance", "condition": "any", "maxReviews": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `specialsCategory` | string | Also include a specials category |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `minRating` | integer | Minimum rating |
| `condition` | string | Condition |
| `sponsoredOnly` | boolean | Sponsored products only |
| `inStockOnly` | boolean | In-stock products only |
| `urls` | array | Product or result URLs |
| `fetchDetails` | boolean | Fetch full product details |
| `maxReviews` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max items |
| `proxy` | object | Proxy configuration |
| `residentialCountries` | array | Preferred exit countries |
| `backupProxyUrl` | string | Backup proxy URL |
| `maxResidentialRequests` | integer | Request cap |
| `trafficBudgetMb` | integer | Traffic budget (MB) |
| `preferDatacenter` | boolean | Prefer the cheaper connection first |
| `autoDowngradeProxy` | boolean | Use the cheaper connection when possib |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bol-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `product_id` | string |
| `id` | string |
| `title` | string |
| `url` | string |
| `sourceUrl` | string |
| `type` | string |
| `mode` | string |
| `brand` | string |
| `category` | string |
| `categories` | list |
| `categoryHierarchy` | list |
| `price` | integer |
| `list_price` | integer |
| `currency` | string |
| `price_currency` | string |
| `discount_percentage` | null |
| `priceRange` | object |
| `buyBoxPriceRange` | object |
| `alternative_prices` | list |
| `isOnSpecial` | boolean |
| `originalPrice` | integer |
| `savingsAmount` | integer |
| `savingsPercent` | null |
| `promoLabel` | string |
| `specialsCategory` | null |
| `condition` | string |
| `availability` | string |
| `in_stock` | boolean |
| `delivery` | string |
| `delivery_text` | string |
| `has_refurbished` | boolean |
| `has_select_deal` | boolean |
| `ean` | null |
| `ean13` | null |
| `gtin13` | null |
| `isbn13` | null |
| `image` | null |
| `images` | null |
| `rating` | float |

---

[← All scrapers](../../README.md)
