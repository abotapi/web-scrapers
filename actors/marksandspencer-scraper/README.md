# Marks & Spencer Scraper

Collect marksandspencer.com (M&S) products and individual reviews from keyword searches, categories or product links. Get prices, all colour galleries, size-level inventory, composition, care, ratings, and review responses, with filters, sorting, resume and recurring updates.

**[Open Marks & Spencer Scraper on Apify](https://apify.com/abotapi/marksandspencer-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~marksandspencer-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["cashmere jumper"], "sortBy": "relevance", "outputType": "products", "reviewSort": "recent", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "maxReviews": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Input mode |
| `searchTerms` | array | Search terms |
| `department` | string | Department |
| `category` | string | Category |
| `brands` | array | Brands |
| `colours` | array | Colours |
| `sizes` | array | Sizes |
| `facet` | array | Additional filters |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum product rating |
| `sortBy` | string | Product sort |
| `urls` | array | Product, category or search links |
| `outputType` | string | Output records |
| `fetchDetails` | boolean | Include product details |
| `reviewSort` | string | Review sort |
| `reviewRatings` | array | Review stars |
| `maxReviewsPerProduct` | integer | Maximum reviews per product |
| `maxPages` | integer | Maximum pages per source |
| `maxItems` | integer | Max items |
| `maxReviews` | integer | Max reviews |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/marksandspencer-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `productId` | string |
| `productExternalId` | string |
| `listingId` | string |
| `url` | string |
| `productUrl` | string |
| `title` | string |
| `name` | string |
| `brand` | string |
| `strokeId` | string |
| `description` | string |
| `price` | integer |
| `priceDetails` | object |
| `previousPrice` | null |
| `unitPrice` | null |
| `currency` | string |
| `averageRating` | float |
| `reviewCount` | integer |
| `images` | list |
| `colours` | list |
| `sizes` | list |
| `variants` | list |
| `fetchedDetails` | boolean |
| `listingData` | object |
| `scrapedAt` | string |
| `searchTerm` | string |
| `searchTotal` | integer |
| `matchedFilters` | object |
| `imageUrl` | string |
| `dietaryInformation` | list |
| `labels` | list |
| `onlineOnly` | boolean |
| `sparksOffers` | list |
| `stockLevelIndicator` | string |
| `productDefinition` | string |
| `isRanged` | boolean |
| `subMessage` | null |
| `productData` | object |
| `composition` | string |

---

[← All scrapers](../../README.md)
