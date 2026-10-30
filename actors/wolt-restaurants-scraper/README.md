# Wolt Scraper

Scrape Wolt restaurants and full menus by city or URL. Extract 60+ fields including restaurant names, addresses, GPS coordinates, opening hours, ratings, tags, menu items, images, prices, delivery zones, fees, minimum orders and merchant details.

**[Open Wolt Scraper on Apify](https://apify.com/abotapi/wolt-restaurants-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wolt-restaurants-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "cities": ["Helsinki"], "sortBy": "default", "language": "en", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `latitude` | number | Latitude |
| `longitude` | number | Longitude |
| `urls` | array | Wolt URLs |
| `primaryCategories` | array | Cuisine filter |
| `minRating` | integer | Min rating score |
| `minRatingVolume` | integer | Min review count |
| `categoryFilter` | string | Category filter (free text) |
| `sortBy` | string | Sort venues by |
| `fetchMenu` | boolean | Fetch full menu |
| `includeDetails` | boolean | Include details |
| `includeReviews` | boolean | Include rating fields |
| `language` | string | Language |
| `maxVenues` | integer | Max venues |
| `maxItems` | integer | Max items |
| `maxVenuesPerCity` | integer | Max venues per city |
| `proxyConfiguration` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wolt-restaurants-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `venueId` | string |
| `slug` | string |
| `name` | string |
| `description` | string |
| `shortDescription` | string |
| `brandSlug` | null |
| `brandName` | null |
| `brandLogoImage` | null |
| `brandLogoBlurhash` | null |
| `coverImage` | string |
| `coverBlurhash` | string |
| `address` | string |
| `city` | string |
| `cityId` | string |
| `citySlug` | string |
| `countryCode` | string |
| `postCode` | string |
| `latitude` | float |
| `longitude` | float |
| `timezone` | string |
| `currency` | string |
| `phone` | string |
| `website` | string |
| `woltUrl` | string |
| `productLine` | string |
| `secondaryProductLine` | string |
| `deliveryMethods` | list |
| `deliveryBasePrice` | integer |
| `deliveryBasePriceFormatted` | string |
| `serviceFeeMin` | integer |
| `serviceFeeMax` | integer |
| `serviceFeePercentage` | integer |
| `orderMinimum` | integer |
| `orderMinimumFormatted` | string |
| `deliveryGeoRange` | object |
| `isPickupFriendly` | boolean |
| `ageVerificationMethod` | string |
| `groupOrderEnabled` | boolean |
| `isWoltPlus` | boolean |
| `ncdAllowed` | boolean |

---

[← All scrapers](../../README.md)
