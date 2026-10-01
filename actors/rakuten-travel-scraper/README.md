# Rakuten Travel Scraper

Scrape Rakuten Travel, Japan's largest domestic hotel-booking site, by prefecture, keyword or URL. Every row carries name, rating, review count, lowest price and access, with optional details: address, phone, facilities, policies, photos and reviews. No API key needed.

**[Open Rakuten Travel Scraper on Apify](https://apify.com/abotapi/rakuten-travel-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rakuten-travel-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["東京"], "sortBy": "recommended", "sortResultsBy": "site_order", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Prefectures and regions |
| `keywords` | array | Keyword searches (optional) |
| `urls` | array | Rakuten Travel URLs |
| `sortBy` | string | Sort the area listing by |
| `minPriceYen` | integer | Minimum price (JPY) |
| `maxPriceYen` | integer | Maximum price (JPY) |
| `minRating` | string | Minimum review score (0 to 5) |
| `sortResultsBy` | string | Order the returned rows by |
| `fetchDetails` | boolean | Fetch full hotel details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per hotel |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max listing pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rakuten-travel-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `hotelNo` | string |
| `rowType` | string |
| `url` | string |
| `name` | string |
| `ratingValue` | float |
| `reviewCount` | integer |
| `minPriceYen` | integer |
| `minPriceTaxIncludedYen` | integer |
| `catchcopy` | string |
| `access` | string |
| `thumbnailUrl` | string |
| `position` | integer |
| `plansUrl` | string |
| `searchSource` | string |
| `areaMiddle` | string |
| `areaSmall` | string |
| `address` | string |
| `phoneNumber` | null |
| `faxNumber` | null |
| `checkInTime` | null |
| `checkOutTime` | null |
| `parking` | string |
| `totalRooms` | null |
| `facilities` | list |
| `roomAmenities` | list |
| `creditCards` | list |
| `meals` | list |
| `privileges` | list |
| `cancellationPolicy` | null |
| `planCancellationPolicy` | null |
| `description` | null |
| `photoUrls` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
