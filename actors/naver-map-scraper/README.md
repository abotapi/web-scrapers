# Naver Map Scraper

Scrape Naver Map places by keyword or URL: names, categories, ratings, phones, addresses, GPS, menus, opening hours, facilities, subway and bus transit, photos, plus visitor and blog reviews. 70+ fields, full pagination, three sort orders, fast and low cost.

**[Open Naver Map Scraper on Apify](https://apify.com/abotapi/naver-map-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~naver-map-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["만두집"], "sort": "relevance", "maxReviews": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `keywords` | array | Search keywords |
| `sort` | string | Sort order |
| `searchCoordinates` | string | Search centre (lat,lng) |
| `startUrls` | array | URLs |
| `includeDetails` | boolean | Include place details |
| `includeReviews` | boolean | Include visitor reviews |
| `maxReviews` | integer | Max reviews per place |
| `maxItems` | integer | Max records |
| `proxy` | object | Proxy |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/naver-map-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `placeId` | string |
| `name` | string |
| `category` | string |
| `businessCategory` | string |
| `categoryCodeList` | list |
| `searchKeyword` | string |
| `placeUrl` | string |
| `latitude` | float |
| `longitude` | float |
| `distance` | string |
| `phone` | string |
| `virtualPhone` | null |
| `address` | string |
| `roadAddress` | string |
| `commonAddress` | string |
| `fullAddress` | string |
| `visitorReviewScore` | float |
| `visitorReviewCount` | integer |
| `totalReviewCount` | null |
| `blogCafeReviewCount` | integer |
| `bookingReviewCount` | integer |
| `imageUrl` | string |
| `imageCount` | integer |
| `imageUrls` | list |
| `options` | null |
| `businessHours` | null |
| `hasBooking` | null |
| `hasNaverPay` | boolean |
| `bookingUrl` | null |
| `talktalkUrl` | null |
| `routeUrl` | null |
| `markerId` | string |
| `newOpening` | null |
| `hasWheelchairEntrance` | null |
| `description` | null |
| `landmark` | string |
| `homepage` | null |
| `conveniences` | list |

---

[← All scrapers](../../README.md)
