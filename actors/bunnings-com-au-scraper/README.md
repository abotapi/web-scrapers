# Bunnings Scraper

Scrape bunnings.com.au products with full specifications, price, brand, stock, image gallery, warranty, customer reviews, rating stats and Q&A. Search by keyword with brand, price, rating and sort filters, or paste product / category / search URLs.

**[Open Bunnings Scraper on Apify](https://apify.com/abotapi/bunnings-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bunnings-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["cordless drill"], "sortBy": "relevance", "productOffers": "any", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Bunnings URLs |
| `brand` | string | Brand |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum rating |
| `productOffers` | string | Product offers |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bunnings-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `code` | string |
| `itemNumber` | string |
| `name` | string |
| `title` | string |
| `brand` | string |
| `brandIconUrl` | string |
| `brandUrl` | string |
| `url` | string |
| `price` | integer |
| `currency` | string |
| `unitOfPrice` | string |
| `rating` | float |
| `ratingCount` | integer |
| `imageUrl` | string |
| `thumbnailUrl` | string |
| `categories` | list |
| `superCategories` | list |
| `keySellingPoints` | list |
| `isActive` | string |
| `bestSeller` | string |
| `newArrival` | string |
| `forHire` | string |
| `trustedSeller` | string |
| `ageRestricted` | string |
| `variantCount` | integer |
| `colorCount` | integer |
| `sizeCount` | integer |
| `size` | integer |
| `fsc` | string |
| `productRanges` | list |
| `offerTypes` | list |
| `isRedemptionOffer` | null |
| `promotion` | null |
| `hasPromotion` | boolean |
| `wasPrice` | null |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `isOnSpecial` | boolean |
| `searchMode` | string |
| `source` | string |

---

[← All scrapers](../../README.md)
