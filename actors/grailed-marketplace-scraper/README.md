# Grailed Scraper

Scrape Grailed by keyword, category, designer, condition, size or URL. Extract prices and price history, descriptions, measurements, shipping, seller profiles and reviews. Includes change tracking to monitor new, updated and removed listings.

**[Open Grailed Scraper on Apify](https://apify.com/abotapi/grailed-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~grailed-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["varsity jacket"], "categories": ["outerwear"], "department": "menswear", "sortResultsBy": "site_order", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `sellerUsernames` | array | Seller usernames |
| `fetchSellerReviews` | boolean | Fetch seller reviews |
| `includeSellerListings` | boolean | Also walk each seller's on-sale listin |
| `categories` | array | Categories |
| `designers` | array | Designers |
| `conditions` | array | Conditions |
| `sizes` | array | Sizes |
| `urls` | array | Grailed URLs |
| `department` | string | Department |
| `minPriceUsd` | integer | Minimum price (USD) |
| `maxPriceUsd` | integer | Maximum price (USD) |
| `sortResultsBy` | string | Order the returned rows by |
| `fetchDetails` | boolean | Fetch listing details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/grailed-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `createdAt` | string |
| `bumpedAt` | string |
| `designer` | string |
| `designers` | list |
| `price` | integer |
| `originalPrice` | integer |
| `askHistory` | list |
| `sold` | boolean |
| `soldAt` | null |
| `soldPrice` | integer |
| `size` | string |
| `condition` | string |
| `conditionLabel` | string |
| `category` | string |
| `categoryPath` | string |
| `department` | string |
| `color` | string |
| `location` | string |
| `strata` | string |
| `styles` | list |
| `badges` | list |
| `buyNow` | boolean |
| `makeOffer` | boolean |
| `photoCount` | integer |
| `coverPhoto` | string |
| `shippingUs` | integer |
| `followerCount` | integer |
| `sellerId` | integer |
| `sellerUsername` | string |
| `sellerUrl` | string |
| `sellerRating` | integer |
| `sellerRatingCount` | integer |
| `sellerSales` | integer |
| `sellerTrusted` | boolean |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
