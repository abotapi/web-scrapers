# mobile.de Scraper

Scrape mobile.de vehicle listings with 30+ fields, including price, registration, mileage, power, fuel, transmission, location and dealer details. Optional enrichment adds descriptions, equipment, image galleries and dealer profiles.

**[Open mobile.de Scraper on Apify](https://apify.com/abotapi/mobile-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mobile-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "vehicleClass": "Car", "country": "DE", "sortBy": "RELEVANCE", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `urls` | array | URLs (URL mode only) |
| `vehicleClass` | string | Vehicle class |
| `make` | string | Make |
| `model` | string | Model |
| `condition` | string | Condition |
| `fuels` | array | Fuel type(s) |
| `transmission` | string | Transmission |
| `bodyType` | string | Body type |
| `country` | string | Listing country |
| `zipcode` | string | Postal code |
| `radiusKm` | integer | Radius around postal code (km) |
| `priceFrom` | integer | Minimum price (EUR) |
| `priceTo` | integer | Maximum price (EUR) |
| `yearFrom` | integer | Minimum first registration year |
| `yearTo` | integer | Maximum first registration year |
| `mileageFrom` | integer | Minimum mileage (km) |
| `mileageTo` | integer | Maximum mileage (km) |
| `powerFromKw` | integer | Minimum power (kW) |
| `powerToKw` | integer | Maximum power (kW) |
| `excludeDamaged` | boolean | Exclude damaged vehicles |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch full vehicle detail |
| `includeSponsored` | boolean | Include sponsored Top-Anzeige listings |
| `maxListings` | integer | Maximum listings |
| `maxPages` | integer | Maximum pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mobile-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `shortTitle` | string |
| `make` | string |
| `model` | string |
| `category` | null |
| `price` | integer |
| `priceFormatted` | string |
| `currency` | string |
| `firstRegistration` | string |
| `mileageKm` | integer |
| `powerKw` | integer |
| `powerHp` | integer |
| `fuel` | string |
| `transmission` | null |
| `city` | null |
| `zip` | null |
| `country` | null |
| `numImages` | integer |
| `previewImage` | string |
| `images` | list |
| `sponsored` | boolean |
| `sellerName` | null |
| `sellerCity` | null |
| `sellerCountry` | null |
| `rating` | float |
| `reviewCount` | integer |
| `description` | null |
| `features` | list |
| `attributes` | object |
| `relativeUrl` | string |

---

[← All scrapers](../../README.md)
