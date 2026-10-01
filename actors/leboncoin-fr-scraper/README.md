# Leboncoin FR Scraper

Pull public leboncoin.fr listings across cars, property, jobs, electronics, furniture, and 35+ categories. Returns 60–78 fields, including price, GPS, seller info, attributes, and images. Search by filters or URL with pagination and listing ID dedupe.

**[Open Leboncoin FR Scraper on Apify](https://apify.com/abotapi/leboncoin-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~leboncoin-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "all", "locations": ["Paris"], "ownerType": "all", "fuel": "all", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AT"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start here, pick your mode |
| `text` | string | Free text query |
| `category` | string | Category |
| `locations` | array | Locations |
| `minSquare` | integer | Min surface area (m²) |
| `maxSquare` | integer | Max surface area (m²) |
| `minMileage` | integer | Min mileage (km) |
| `maxMileage` | integer | Max mileage (km) |
| `urls` | array | Search URLs |
| `ownerType` | string | Seller type |
| `minPrice` | integer | Min price (EUR) |
| `maxPrice` | integer | Max price (EUR) |
| `rooms` | array | Number of rooms |
| `fuel` | string | Fuel type |
| `sortBy` | string | Sort order |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total listings |
| `fetchDetails` | boolean | Fetch detail pages (richer fields) |
| `fetchSellerReviews` | boolean | Enrich with seller reviews |
| `fetchSellerOtherListings` | boolean | Enrich with seller's other listings |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/leboncoin-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `list_id` | integer |
| `subject` | string |
| `body` | string |
| `url` | string |
| `category_id` | string |
| `category_name` | string |
| `ad_type` | string |
| `status` | string |
| `brand` | string |
| `price` | integer |
| `price_max` | null |
| `price_cents` | integer |
| `publication_date` | string |
| `index_date` | string |
| `expiration_date` | null |
| `has_phone` | boolean |
| `is_boosted` | boolean |
| `is_urgent` | boolean |
| `city` | string |
| `zipcode` | string |
| `department_id` | string |
| `department` | string |
| `region_id` | string |
| `region` | string |
| `country_id` | string |
| `latitude` | float |
| `longitude` | float |
| `owner_type` | string |
| `owner_name` | string |
| `owner_user_id` | string |
| `owner_store_id` | string |
| `owner_no_salesmen` | boolean |
| `owner_raw` | object |
| `image_count` | integer |
| `thumb_url` | string |
| `small_url` | string |
| `image_urls` | list |
| `view_count` | null |
| `favorite_count` | null |

---

[← All scrapers](../../README.md)
