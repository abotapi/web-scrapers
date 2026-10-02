# Carsales.com.au Scraper

Scrape structured vehicle listings from Carsales.com.au from $1 per 1K results. Built to bypass the 20-page / 440-car search cap with deep filtering. Returns clean JSON with 30+ fields per listing, ideal for dealers, analysts, pricing tools, and real-time vehicle data pipelines.

**[Open Carsales.com.au Scraper on Apify](https://apify.com/abotapi/carsales-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~carsales-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "condition": "used", "sellerType": "all", "sortBy": "featured", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `urls` | array | URLs (URL mode only) |
| `condition` | string | Condition |
| `sellerType` | string | Seller type |
| `make` | string | Make |
| `model` | string | Model |
| `bodyType` | string | Body type |
| `state` | string | State |
| `transmission` | string | Transmission |
| `fuelType` | string | Fuel type |
| `colour` | string | Colour |
| `cylinders` | integer | Cylinders |
| `doors` | integer | Doors |
| `priceMin` | integer | Minimum price (AUD) |
| `priceMax` | integer | Maximum price (AUD) |
| `yearMin` | integer | Minimum year |
| `yearMax` | integer | Maximum year |
| `odometerMin` | integer | Minimum odometer (km) |
| `odometerMax` | integer | Maximum odometer (km) |
| `postcode` | string | Postcode |
| `radiusKm` | integer | Radius (km) |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch full details |
| `maxListings` | integer | Maximum listings |
| `expandPriceBands` | boolean | Deep collection (beyond one search's 4 |
| `maxPages` | integer | Maximum pages per search |
| `proxyConfiguration` | object | Proxy configuration (RESIDENTIAL requi |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/carsales-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `make` | string |
| `model` | string |
| `year` | integer |
| `variant` | string |
| `bodyType` | string |
| `transmission` | string |
| `engine` | string |
| `fuelType` | string |
| `cylinders` | null |
| `engineCapacity` | string |
| `odometer` | integer |
| `odometerDisplay` | string |
| `price` | integer |
| `priceDisplay` | string |
| `priceDriveAway` | null |
| `priceDriveAwayDisplay` | string |
| `currency` | string |
| `priceInfo` | string |
| `condition` | string |
| `adType` | string |
| `sellerType` | string |
| `sellerId` | string |
| `state` | string |
| `badges` | list |
| `certificationBadge` | string |
| `marketIndicator` | string |
| `rankingType` | string |
| `silo` | string |
| `suggestedResult` | boolean |
| `images` | list |
| `imageCount` | integer |
| `videoCount` | integer |
| `threeSixtyCount` | integer |
| `tracking` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
