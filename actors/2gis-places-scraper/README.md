# 2GIS Scraper

Extract business and place data from 2GIS.com at scale. Get names, addresses, phones, emails, websites, social links, opening hours, ratings, reviews, photos, coordinates, and 80+ fields per place. Supports all regions covered by 2GIS with fast, low-cost extraction.

**[Open 2GIS Scraper on Apify](https://apify.com/abotapi/2gis-places-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~2gis-places-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": ["кофейня"], "city": "Москва", "language": "ru", "sortBy": "relevance", "maxReviews": 10, "reviewsSort": "date_edited", "reviewsProvider": "all", "reviewsRating": "all", "maxResults": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | array | Search queries |
| `categoryQuery` | array | Categories |
| `latitude` | string | Latitude (WHERE) |
| `longitude` | string | Longitude (WHERE) |
| `radiusMeters` | integer | Radius (meters) |
| `bbox` | string | Map area / bounding box (WHERE) |
| `urls` | array | 2GIS URLs or IDs |
| `city` | string | City (WHERE) |
| `language` | string | Language |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum rating |
| `minReviews` | integer | Minimum review count |
| `onlyWithPhone` | boolean | Only places with a phone |
| `onlyWithWebsite` | boolean | Only places with a website |
| `skipAds` | boolean | Skip promoted places |
| `maxReviews` | integer | Max reviews per place |
| `reviewsSort` | string | Reviews sort |
| `reviewsProvider` | string | Reviews source |
| `reviewsRating` | string | Reviews rating filter |
| `reviewsMinRating` | string | Reviews minimum rating |
| `reviewsWithAnswer` | boolean | Only reviews with an official answer |
| `reviewsStartDate` | string | Reviews from date |
| `reviewsKeyword` | string | Reviews keyword |
| `includePhotos` | boolean | Include place photos |
| `maxResults` | integer | Max places (total) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/2gis-places-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `fullId` | string |
| `name` | string |
| `fullName` | string |
| `shortName` | string |
| `nameExtension` | string |
| `url` | string |
| `type` | string |
| `subtype` | null |
| `purpose` | string |
| `description` | null |
| `rubrics` | list |
| `rubricIds` | list |
| `primaryRubric` | string |
| `rating` | float |
| `reviewCount` | integer |
| `ratingCount` | integer |
| `isReviewable` | boolean |
| `orgRating` | float |
| `orgReviewCount` | integer |
| `flampRating` | null |
| `flampReviewCount` | null |
| `address` | string |
| `fullAddress` | string |
| `addressComment` | null |
| `postcode` | string |
| `buildingId` | string |
| `country` | string |
| `region` | string |
| `city` | string |
| `district` | string |
| `livingArea` | null |
| `street` | string |
| `houseNumber` | string |
| `latitude` | float |
| `longitude` | float |
| `timezoneOffset` | integer |
| `nearestStations` | list |
| `buildingName` | null |

---

[← All scrapers](../../README.md)
