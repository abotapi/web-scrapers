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
  -d '{"mode": "search", "outputType": "listings", "category": "home-garden-shops", "limit": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `outputType` | string | Output |
| `category` | string | Category Slug |
| `searchQuery` | string | Search Query |
| `location` | string | Location |
| `showDiscontinued` | boolean | Show Discontinued |
| `sortBy` | string | Sort Results By |
| `urls` | array | URLs |
| `limit` | integer | Max Output Rows |
| `maxConcurrency` | integer | Max Concurrency |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/product-reviews-australia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
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
| `scrapedAt` | string |
| `reviews` | list |
| `totalReviews` | integer |
| `reviewPages` | integer |
| `pagesScraped` | integer |
| `address` | null |
| `businessHours` | null |
| `description` | string |
| `faqs` | list |
| `specifications` | object |

---

[← All scrapers](../../README.md)
