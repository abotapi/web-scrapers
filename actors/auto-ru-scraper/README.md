# Auto.ru Scraper

Scrape Auto.ru car listings: search by make, model, year, price, mileage, body, engine, gearbox, drive, seller and region, or paste result, dealer and listing links. Get price history, vehicle checks, owners, valuation, dealer details and photos, plus price-change tracking.

**[Open Auto.ru Scraper on Apify](https://apify.com/abotapi/auto-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~auto-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "vehicles": ["bmw x5"], "condition": "any", "steeringWheel": "any", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `vehicles` | array | Makes and models |
| `condition` | string | Condition |
| `regions` | array | Regions |
| `regionRadiusKm` | integer | Search radius around a city (km) |
| `dealerIds` | array | Dealer ids |
| `yearFrom` | integer | Year from |
| `yearTo` | integer | Year to |
| `priceFrom` | integer | Price from (RUB) |
| `priceTo` | integer | Price to (RUB) |
| `mileageFrom` | integer | Mileage from (km) |
| `mileageTo` | integer | Mileage to (km) |
| `engineVolumeFrom` | integer | Engine volume from (cm³) |
| `engineVolumeTo` | integer | Engine volume to (cm³) |
| `powerFrom` | integer | Power from (hp) |
| `powerTo` | integer | Power to (hp) |
| `bodyTypes` | array | Body types |
| `engineTypes` | array | Engine types |
| `transmissions` | array | Transmissions |
| `driveTypes` | array | Drive types |
| `sellerTypes` | array | Seller types |
| `steeringWheel` | string | Steering wheel |
| `maxOwners` | integer | Max previous owners |
| `includeDamaged` | boolean | Include damaged cars |
| `includeNotCleared` | boolean | Include cars not cleared through custo |
| `sortBy` | string | Sort by |
| `urls` | array | Links |
| `listingIds` | array | Listing keys |
| `fetchDetails` | boolean | Read each listing's page |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max result pages per search |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Changes to watch (incremental mode onl |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after missed scans (incremental |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/auto-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `listingId` | string |
| `offerId` | string |
| `url` | string |
| `title` | string |
| `condition` | string |
| `status` | string |
| `damaged` | boolean |
| `availability` | string |
| `make` | string |
| `makeName` | string |
| `model` | string |
| `modelName` | string |
| `generation` | string |
| `generationYearFrom` | integer |
| `generationYearTo` | integer |
| `complectation` | string |
| `year` | integer |
| `mileageKm` | integer |
| `bodyType` | string |
| `bodyTypeCode` | string |
| `bodyTypeGroup` | string |
| `doors` | integer |
| `seats` | integer |
| `autoClass` | string |
| `engineType` | string |
| `engineVolumeCc` | integer |
| `enginePowerHp` | integer |
| `enginePowerKw` | integer |
| `engineName` | string |
| `transmission` | string |
| `driveType` | string |
| `steeringWheel` | string |
| `acceleration0to100` | float |
| `clearanceMm` | integer |
| `trunkVolumeL` | integer |
| `fuelRateL100km` | null |
| `electricRangeKm` | null |
| `colorHex` | string |
| `color` | string |

---

[← All scrapers](../../README.md)
