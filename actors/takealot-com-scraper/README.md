# Willhaben.at Scraper

Scrape Willhaben.at listings into clean JSON with 40+ structured fields, including prices, GPS coordinates, photos, dates, seller details and category-specific attributes. Search with filters or paste any Willhaben URL.

**[Open Willhaben.at Scraper on Apify](https://apify.com/abotapi/takealot-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~takealot-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["laptop"], "sort": "Relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `sort` | string | Sort order |
| `urls` | array | takealot.com links |
| `brand` | string | Brand filter |
| `minPrice` | integer | Min price (ZAR) |
| `maxPrice` | integer | Max price (ZAR) |
| `minRating` | string | Minimum star rating |
| `inStockRegion` | string | In stock at |
| `dealType` | string | Deals filter |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch written reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per keyword |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/takealot-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `plid` | integer |
| `url` | string |
| `title` | string |
| `subtitle` | string |
| `brand` | null |
| `price` | integer |
| `priceMax` | integer |
| `prettyPrice` | string |
| `listingPrice` | null |
| `savingPercent` | integer |
| `currency` | string |
| `starRating` | float |
| `reviewCount` | integer |
| `ratingDistribution` | object |
| `inStock` | boolean |
| `stockStatus` | string |
| `isImportedItem` | boolean |
| `distributionCentres` | list |
| `isPreorder` | boolean |
| `addToCartAvailable` | boolean |
| `isDeal` | boolean |
| `badges` | list |
| `imageUrl` | string |
| `imageCount` | integer |
| `shippingMessage` | string |
| `shippingCode` | string |
| `isPromotion` | boolean |
| `tsin` | integer |
| `productId` | integer |
| `hasMoreColours` | boolean |
| `promotionLabel` | null |
| `descriptionHtml` | string |
| `descriptionText` | string |
| `specs` | object |
| `boxContents` | string |
| `warranty` | string |
| `categoriesPath` | list |
| `departmentName` | string |

---

[← All scrapers](../../README.md)
