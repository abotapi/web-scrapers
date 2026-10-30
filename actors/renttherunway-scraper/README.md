# Rent the Runway Scraper

Scrape Rent the Runway (renttherunway.com) designer clothing and accessories by category, keyword or URL. Extract brands, product titles, rental and retail prices, sizes, availability, images, ratings and member reviews.

**[Open Rent the Runway Scraper on Apify](https://apify.com/abotapi/renttherunway-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~renttherunway-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "categories": ["dresses"], "sortBy": "recommended", "availabilityScope": "all", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `categories` | array | Categories |
| `searchText` | string | Search term |
| `sizes` | array | Sizes |
| `sortBy` | string | Sort |
| `availabilityScope` | string | Availability scope |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch member reviews |
| `maxReviews` | integer | Max reviews per style |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy and connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/renttherunway-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `styleId` | string |
| `url` | string |
| `designer` | string |
| `title` | string |
| `category` | string |
| `breadcrumbs` | list |
| `rentalPrice` | integer |
| `retailPrice` | integer |
| `msrp` | integer |
| `priceCurrency` | string |
| `availability` | string |
| `inStock` | boolean |
| `shortDescription` | string |
| `description` | string |
| `sizesAvailable` | list |
| `sizeRange` | string |
| `modelInfo` | list |
| `materialsAndMeasurements` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `ratingValue` | null |
| `reviewCount` | null |
| `reviewAverageRating` | null |
| `reviewFitCounts` | null |
| `reviewPhotoCount` | null |
| `reviews` | list |
| `datePublished` | string |
| `dateModified` | string |
| `scopePath` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
