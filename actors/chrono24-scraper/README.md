# Chrono24 Scraper

Scrape Chrono24 luxury watch listings by keyword, filters or URL. Extract 50+ fields including brand, model, reference number, price, year, condition, movement, case specifications, seller details, location, images and more.

**[Open Chrono24 Scraper on Apify](https://apify.com/abotapi/chrono24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~chrono24-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQuery": "Rolex Submariner", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQuery` | string | Search keyword |
| `searchParams` | object | Filters |
| `sortBy` | string | Sort by |
| `dealsOnly` | boolean | Top Deals collection only |
| `urls` | array | Start URLs |
| `fetchDetails` | boolean | Fetch full details |
| `fetchSellerReviews` | boolean | Include seller reviews |
| `flatten` | boolean | Flatten specs |
| `includeRaw` | boolean | Include raw size marker |
| `maxListings` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/chrono24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `listingId` | string |
| `watchId` | string |
| `listingUrl` | string |
| `sourceUrl` | string |
| `title` | string |
| `brand` | string |
| `model` | string |
| `referenceNumber` | string |
| `listingCode` | string |
| `description` | string |
| `price` | integer |
| `priceDisplay` | string |
| `currency` | string |
| `availability` | string |
| `availabilityText` | string |
| `condition` | string |
| `conditionText` | string |
| `year` | string |
| `location` | string |
| `sellerCountry` | string |
| `sellerUsername` | string |
| `merchantCountry` | string |
| `certificationStatus` | string |
| `isDeal` | boolean |
| `scopeOfDelivery` | string |
| `gender` | null |
| `productType` | string |
| `marketingType` | string |
| `collectionId` | integer |
| `modelId` | integer |
| `modelVariantId` | integer |
| `refId` | integer |
| `buyingAgent` | null |
| `specs` | object |
| `images` | list |
| `thumbnail` | string |
| `scrapedAt` | string |
| `sellerRating` | float |
| `reviewCount` | integer |

---

[← All scrapers](../../README.md)
