# Depop Scraper

Scrape Depop search results, listings, shops, and reviews to JSON, CSV, or Excel. Extract titles, prices, shipping, brands, conditions, colours, sizes, photos, descriptions, and seller profiles.

**[Open Depop Scraper on Apify](https://apify.com/abotapi/depop-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~depop-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["nike vintage"], "sortBy": "relevance", "gender": "any", "sellers": ["mishmoshmart"], "reviewRole": "seller", "country": "us", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search Keywords |
| `sortBy` | string | Sort By |
| `minPrice` | integer | Min Price |
| `maxPrice` | integer | Max Price |
| `gender` | string | Gender Department |
| `brands` | array | Brand IDs |
| `categories` | array | Category IDs |
| `colours` | array | Colours |
| `conditions` | array | Conditions |
| `groups` | array | Department Groups |
| `sizes` | array | Size IDs |
| `urls` | array | URLs |
| `sellers` | array | Sellers |
| `reviewRole` | string | Review Role |
| `country` | string | Marketplace Country |
| `maxPages` | integer | Max Pages Per Search |
| `maxListings` | integer | Max Items (Total) |
| `fetchDetails` | boolean | Fetch Item Details |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/depop-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `slug` | string |
| `url` | string |
| `status` | string |
| `isOnSale` | boolean |
| `brandId` | string |
| `brandName` | string |
| `countryCode` | string |
| `hasVideo` | boolean |
| `likeCount` | integer |
| `isLiked` | boolean |
| `pictures` | list |
| `mainPicture` | string |
| `pictureCount` | integer |
| `sizes` | list |
| `variantSetId` | integer |
| `variants` | list |
| `sku` | null |
| `isBoosted` | boolean |
| `boostedAt` | string |
| `isSold` | null |
| `price` | integer |
| `totalPrice` | integer |
| `buyerFee` | integer |
| `tax` | integer |
| `taxType` | string |
| `shippingCost` | float |
| `shippingBoundary` | string |
| `shippingId` | string |
| `nationalShippingCost` | null |
| `nationalShippingType` | null |
| `priceType` | null |
| `currency` | string |
| `isReduced` | boolean |
| `discountPercentage` | null |
| `originalPriceBeforeDiscount` | null |
| `hasBuyerFee` | boolean |
| `hasTax` | boolean |
| `hasShippingPrice` | boolean |
| `description` | string |

---

[← All scrapers](../../README.md)
