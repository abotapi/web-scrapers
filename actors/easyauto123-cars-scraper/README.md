# EasyAuto123 Scraper

Scrape EasyAuto123 vehicle listings into clean structured data. Extract prices, VINs, odometer readings, make, model, year, trim, specs, images, dealer names, locations, contact details, listing URLs, and optional extra fields for market research, lead generation, and inventory tracking.

**[Open EasyAuto123 Scraper on Apify](https://apify.com/abotapi/easyauto123-cars-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~easyauto123-cars-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "sort": "price-reduced", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `urls` | array | EasyAuto123 URLs |
| `keywords` | array | Keywords |
| `makes` | array | Makes |
| `models` | array | Models |
| `variants` | array | Variants |
| `locations` | array | Locations |
| `vehicleTypes` | array | Vehicle types |
| `fuelTypes` | array | Fuel types |
| `transmissions` | array | Transmissions |
| `colours` | array | Colours |
| `lifestyles` | array | Lifestyles |
| `vehicleSizes` | array | Vehicle sizes |
| `carTypes` | array | Car types |
| `minYear` | integer | Minimum year |
| `maxYear` | integer | Maximum year |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minOdometer` | integer | Minimum odometer |
| `maxOdometer` | integer | Maximum odometer |
| `sort` | string | Sort |
| `fetchDetails` | boolean | Fetch detail fields |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/easyauto123-cars-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `make` | string |
| `model` | string |
| `variant` | string |
| `year` | integer |
| `price` | integer |
| `priceType` | string |
| `state` | string |
| `location` | string |
| `region` | string |
| `siteCode` | string |
| `odometer` | integer |
| `vin` | string |
| `fuelType` | string |
| `transmission` | string |
| `driveType` | string |
| `engineCapacity` | string |
| `colour` | string |
| `vehicleTypes` | list |
| `fuelConsumption` | string |
| `carType` | string |
| `banner` | string |
| `status` | string |
| `updatedAt` | string |
| `primaryImage` | string |
| `imageUrls` | list |
| `imageCount` | integer |
| `contractPrice` | list |
| `storeName` | string |
| `storeEmail` | string |
| `storePhone` | string |
| `storeAddress` | string |
| `storeRating` | float |
| `storeRaw` | object |
| `detailFetched` | boolean |
| `productCategory` | string |
| `availableSince` | string |
| `ancapRating` | string |

---

[← All scrapers](../../README.md)
