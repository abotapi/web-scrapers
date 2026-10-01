# Domclick RU Property Scraper

Extract property listings from domclick.ru, one of Russia’s largest real estate portals. Search by city or use listing/search URLs. Returns 70+ fields including price, area, rooms, floor, address, GPS, metro info, photos, seller and agency details, developer data, discounts, and mortgage flags.

**[Open Domclick RU Property Scraper on Apify](https://apify.com/abotapi/domclick-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~domclick-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Москва"], "dealType": "sale", "category": "living", "offerType": "flat", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "RU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Cities or regions |
| `dealType` | string | Deal type |
| `category` | string | Category |
| `offerType` | string | Property type |
| `rooms` | array | Rooms |
| `minPrice` | integer | Min price () |
| `maxPrice` | integer | Max price () |
| `minArea` | integer | Min area (m²) |
| `maxArea` | integer | Max area (m²) |
| `minFloor` | integer | Min floor |
| `maxFloor` | integer | Max floor |
| `sortBy` | string | Sort by |
| `urls` | array | Domclick URLs |
| `fetchDetails` | boolean | Fetch extra details (valuation, nearby |
| `maxPages` | integer | Max pages per target |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/domclick-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `offerType` | string |
| `dealType` | string |
| `status` | integer |
| `isSold` | boolean |
| `price` | integer |
| `squarePrice` | integer |
| `monthlyPayment` | integer |
| `currency` | string |
| `area` | integer |
| `rooms` | integer |
| `roomsOffered` | integer |
| `floor` | integer |
| `totalFloors` | integer |
| `buildYear` | integer |
| `isApartment` | boolean |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `nearestSubway` | string |
| `subwayWalkMinutes` | integer |
| `subways` | list |
| `description` | string |
| `photoCount` | integer |
| `photos` | list |
| `hasVideo` | boolean |
| `complexId` | integer |
| `complexName` | string |
| `complexSlug` | string |
| `buildingReleased` | boolean |
| `buildingEndYear` | integer |
| `buildingEndQuarter` | integer |
| `sellerName` | string |
| `sellerCasId` | null |
| `sellerExperience` | null |
| `sellerPhotoUrl` | null |
| `isAgent` | boolean |
| `isAgency` | boolean |
| `isSbolVerified` | boolean |

---

[← All scrapers](../../README.md)
