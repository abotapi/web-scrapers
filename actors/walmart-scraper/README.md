# Walmart Scraper

Scrape Walmart.com by keyword, URL, or item ID. Extract prices, was-prices, sellers, marketplace offers, stock, ratings, specs, images, and reviews. Track NEW, UPDATED, REAPPEARED, and EXPIRED items with resume and MCP export.

**[Open Walmart Scraper on Apify](https://apify.com/abotapi/walmart-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~walmart-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["laptop"], "sortBy": "best_match", "retailerType": "any", "condition": "any", "specialOffer": "any", "minRating": "any", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `searchUrls` | array | Storefront links (search, browse, shop |
| `productInputs` | array | Product links or item ids |
| `sortBy` | string | Sort by |
| `brands` | array | Brands |
| `retailerType` | string | Sold by |
| `condition` | string | Item condition |
| `specialOffer` | string | Deals |
| `minRating` | string | Minimum customer rating |
| `inStockOnly` | boolean | Only items available now |
| `excludeSponsored` | boolean | Hide sponsored results |
| `minPrice` | integer | Minimum price (USD) |
| `maxPrice` | integer | Maximum price (USD) |
| `fetchDetails` | boolean | Fetch product details |
| `includeReviews` | boolean | Include customer reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/walmart-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `itemId` | string |
| `productId` | string |
| `url` | string |
| `title` | string |
| `brand` | null |
| `shortDescription` | null |
| `imageUrl` | string |
| `price` | integer |
| `wasPrice` | null |
| `priceRangeLow` | float |
| `priceRangeHigh` | null |
| `currency` | string |
| `rating` | float |
| `reviewCount` | integer |
| `sellerName` | string |
| `sellerId` | string |
| `sellerType` | null |
| `availabilityStatus` | string |
| `inStock` | boolean |
| `fulfillmentText` | string |
| `badges` | list |
| `sponsored` | boolean |
| `variantCount` | integer |
| `offerId` | string |
| `categoryPath` | string |
| `categoryPathId` | string |
| `itemType` | string |
| `searchQuery` | string |
| `sourceUrl` | string |
| `resultPage` | integer |
| `resultPosition` | integer |

---

[← All scrapers](../../README.md)
