# Autotrader US Scraper

Scrape US car listings from Autotrader by make, model, ZIP, price, year, body style, filters, or listing URLs. Returns VIN, price, KBB deal rating, mileage, colors, MPG, drivetrain, dealer name, phone, location, history flags, photos, and 60+ fields.

**[Open Autotrader US Scraper on Apify](https://apify.com/abotapi/autotrader-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~autotrader-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "zip": "90012", "make": ["HONDA"], "sellerType": "any", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `zip` | string | ZIP code |
| `searchRadius` | integer | Search radius (miles) |
| `make` | array | Make(s) |
| `model` | array | Model(s) |
| `minYear` | integer | Minimum year |
| `maxYear` | integer | Maximum year |
| `minPrice` | integer | Minimum price (USD) |
| `maxPrice` | integer | Maximum price (USD) |
| `maxMileage` | integer | Maximum mileage |
| `condition` | array | Condition |
| `bodyStyle` | array | Body style |
| `fuelType` | array | Fuel type |
| `driveType` | array | Drivetrain |
| `transmission` | array | Transmission |
| `exteriorColor` | array | Exterior color |
| `vehicleHistory` | array | Vehicle history |
| `dealType` | array | Deal rating |
| `sellerType` | string | Seller type |
| `sortBy` | string | Sort by |
| `urls` | array | Autotrader URLs |
| `fetchDetails` | boolean | Fetch full detail per listing |
| `maxListings` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |
| `sessionCookie` | string | Session cookie (optional, advanced) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/autotrader-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `vin` | string |
| `url` | string |
| `title` | string |
| `year` | integer |
| `make` | string |
| `makeCode` | string |
| `model` | string |
| `modelCode` | string |
| `trim` | string |
| `bodyStyle` | object |
| `listingType` | string |
| `condition` | string |
| `price` | integer |
| `displayPrice` | integer |
| `priceLabel` | string |
| `dealIndicator` | string |
| `kbbFairPurchasePrice` | integer |
| `kbbPriceDelta` | integer |
| `kbbPriceLow` | integer |
| `kbbPriceHigh` | integer |
| `isReducedPrice` | boolean |
| `hasSpecialOffer` | boolean |
| `mileage` | string |
| `mileageUnit` | null |
| `exteriorColor` | string |
| `exteriorColorSimple` | string |
| `interiorColor` | string |
| `engine` | string |
| `fuelType` | string |
| `transmission` | string |
| `driveType` | string |
| `doors` | string |
| `mpgCity` | integer |
| `mpgHighway` | integer |
| `hasLeatherSeats` | boolean |
| `daysOnSite` | integer |
| `isNewlyListed` | boolean |
| `isHot` | boolean |
| `stockId` | string |

---

[← All scrapers](../../README.md)
