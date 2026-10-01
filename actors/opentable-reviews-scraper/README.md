# OpenTable Reviews Scraper

Scrape full OpenTable.com restaurant reviews by keyword, area, or restaurant profile URLs. Collect every available review with text, ratings, diner profile data, tags, photos, restaurant metadata, cuisines, neighborhood, and profile links in structured rows.

**[Open OpenTable Reviews Scraper on Apify](https://apify.com/abotapi/opentable-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~opentable-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["sushi"], "location": "New York", "maxItems": 10, "maxReviewsPerRestaurant": 10, "reviewSort": "highestRated", "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Input mode |
| `keywords` | array | Keywords |
| `location` | string | Location |
| `latitude` | number | Latitude (advanced) |
| `longitude` | number | Longitude (advanced) |
| `startUrls` | array | OpenTable restaurant URLs |
| `maxItems` | integer | Max items |
| `maxReviewsPerRestaurant` | integer | Max reviews per restaurant |
| `maxRestaurants` | integer | Max restaurants per keyword |
| `reviewSort` | string | Review sort order |
| `minOverallRating` | number | Minimum overall rating |
| `minFoodRating` | number | Minimum food rating |
| `minServiceRating` | number | Minimum service rating |
| `minAmbienceRating` | number | Minimum ambience rating |
| `minValueRating` | number | Minimum value rating |
| `cuisines` | array | Cuisine filter |
| `neighborhoods` | array | Neighborhood filter |
| `fromDinedDate` | string | Dined from |
| `toDinedDate` | string | Dined to |
| `vipOnly` | boolean | VIP reviewers only |
| `requireReviewPhotos` | boolean | Require review photos |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/opentable-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `reviewId` | string |
| `reviewText` | string |
| `ratingOverall` | integer |
| `ratingFood` | integer |
| `ratingService` | integer |
| `ratingAmbience` | integer |
| `ratingValue` | integer |
| `ratingNoise` | string |
| `reviewType` | string |
| `submittedDateTime` | string |
| `dinedDateTime` | string |
| `dinedDate` | string |
| `reviewHelpfulUp` | integer |
| `reviewHelpfulDown` | integer |
| `reviewHelpfulScore` | integer |
| `restaurantReplyText` | null |
| `reviewerName` | string |
| `reviewerInitials` | string |
| `reviewerIsVip` | null |
| `reviewerLocation` | string |
| `reviewerApprovedReviewCount` | integer |
| `reviewerProfileColor` | string |
| `reviewerPhotoUrl` | null |
| `reviewPhotoUrls` | list |
| `reviewPhotoCount` | integer |
| `restaurantId` | integer |
| `restaurantName` | string |
| `restaurantUrl` | string |
| `restaurantMetro` | string |
| `restaurantMacro` | string |
| `restaurantNeighborhood` | string |
| `restaurantPrimaryCuisine` | string |
| `restaurantCuisines` | list |
| `restaurantPriceBand` | integer |
| `restaurantCurrencySymbol` | string |
| `restaurantRating` | float |
| `restaurantPhotoUrl` | string |
| `restaurantTotalReviewCount` | integer |
| `sourceMode` | string |
| `sourceQuery` | string |

---

[← All scrapers](../../README.md)
