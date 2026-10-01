# FurnishedFinder Scraper

Scrape furnishedfinder.com listings by city or URL. Extract structured data including price, beds, baths, occupancy, amenities, photos, location, square footage, ratings, reviews, utilities, house rules, and fees. Fast and reliable via the site's data API.

**[Open FurnishedFinder Scraper on Apify](https://apify.com/abotapi/furnishedfinder-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~furnishedfinder-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Houston, TX"], "propertyTypeClass": "any", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Cities |
| `propertyTypeClass` | string | Property type |
| `minPrice` | integer | Min monthly price (USD) |
| `maxPrice` | integer | Max monthly price (USD) |
| `minBedrooms` | integer | Min bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch full property details |
| `fetchReviews` | boolean | Include guest reviews |
| `maxPages` | integer | Max pages per city |
| `maxListings` | integer | Max listings (total, default 20, 0  un |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/furnishedfinder-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `propertyId` | string |
| `unitId` | string |
| `url` | string |
| `name` | string |
| `propertyType` | string |
| `propertyTypeClass` | string |
| `bedroomCount` | integer |
| `bathroomCount` | integer |
| `bathroomType` | null |
| `totalSleeps` | integer |
| `laundryType` | string |
| `priceFormatted` | string |
| `priceValue` | integer |
| `priceCurrency` | string |
| `latitude` | float |
| `longitude` | float |
| `city` | string |
| `state` | string |
| `encodedLocationName` | string |
| `isAvailableNow` | boolean |
| `availableOnDate` | string |
| `minimumStayInDays` | integer |
| `amenities` | list |
| `photos` | list |
| `photoCount` | integer |
| `searchLocation` | string |
| `description` | string |
| `neighborhoodDescription` | string |
| `spaceDescription` | string |
| `squareFootage` | integer |
| `avgRating` | integer |
| `totalReviewCount` | integer |
| `reviews` | null |
| `utilitiesIncluded` | boolean |
| `minimumStayDays` | integer |
| `houseRules` | list |
| `fees` | list |
| `detailAmenities` | list |
| `bedroomsDetail` | list |

---

[← All scrapers](../../README.md)
