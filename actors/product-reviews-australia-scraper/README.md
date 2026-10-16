# ProductReview.com.au Scraper

Scrape ProductReview.com.au products, businesses and customer reviews. Search by location, category or custom query with advanced filters. Extract business details, ratings, review content and structured review insights.

**[Open ProductReview.com.au Scraper on Apify](https://apify.com/abotapi/product-reviews-australia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~product-reviews-australia-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "outputType": "listings", "category": "home-garden-shops", "maxReviewsPerListing": 10, "limit": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `outputType` | string | Output |
| `category` | string | Category (Filter mode only) |
| `searchQuery` | string | Search Query |
| `location` | string | Location Slug or Name |
| `showDiscontinued` | boolean | Show Discontinued |
| `sortBy` | string | Sort Results By (Filter mode only) |
| `brands` | array | Brands |
| `minRating` | integer | Minimum listing rating |
| `urls` | array | URLs |
| `maxReviewsPerListing` | integer | Max reviews per listing |
| `reviewRating` | integer | Only reviews with this rating |
| `reviewVerifiedOnly` | boolean | Verified purchases only |
| `reviewsWithAttachmentsOnly` | boolean | Only reviews with photos/attachments |
| `reviewSortBy` | string | Sort reviews by |
| `limit` | integer | Max Output Rows (applies to both modes |
| `maxConcurrency` | integer | Max Concurrency |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/product-reviews-australia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `name` | string |
| `slug` | string |
| `detailsUrl` | string |
| `brand` | object |
| `contact` | object |
| `categories` | list |
| `locations` | list |
| `statistics` | object |
| `isDiscontinued` | boolean |
| `featuredReview` | object |
| `highlightedReviews` | list |
| `logoUrl` | string |
| `pictureUrl` | string |
| `pictures` | list |
| `createdAt` | string |
| `fullName` | string |
| `shortName` | string |
| `lowestPrice` | null |
| `lowestPriceFormatted` | null |
| `offers` | list |
| `reviewsSummary` | string |
| `reviewsSummaryUpdatedAt` | string |
| `reviewsSummaryHighlights` | object |
| `marketAvailability` | object |
| `tags` | list |
| `awardYears` | list |
| `officialLink` | string |
| `specificationValues` | object |
| `universalIds` | list |
| `videos` | list |
| `specHighlights` | list |
| `capacityText` | null |
| `rrpPrice` | null |
| `scrapedAt` | string |
| `searchUrl` | string |
| `reviews` | list |
| `reviewsCollected` | integer |
| `totalReviews` | integer |

---

[← All scrapers](../../README.md)
