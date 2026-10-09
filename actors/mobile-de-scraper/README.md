# mobile.de Scraper

Scrape mobile.de vehicle listings with 30+ fields including price, mileage, registration, power, fuel, transmission, location and dealer details. Optional enrichment adds descriptions, equipment, images and dealer profiles.

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
| `vehicleClass` | string | Vehicle class |
| `make` | string | Make |
| `model` | string | Model |
| `condition` | string | Condition |
| `fuels` | array | Fuel type(s) |
| `transmission` | string | Transmission |
| `bodyType` | string | Body type |
| `country` | string | Listing country |
| `zipcode` | string | Location (postal code or town) |
| `radiusKm` | integer | Radius around location (km) |
| `priceFrom` | integer | Minimum price (EUR) |
| `priceTo` | integer | Maximum price (EUR) |
| `yearFrom` | integer | Minimum first registration year |
| `yearTo` | integer | Maximum first registration year |
| `mileageFrom` | integer | Minimum mileage (km) |
| `mileageTo` | integer | Maximum mileage (km) |
| `powerFromKw` | integer | Minimum power (kW) |
| `powerToKw` | integer | Maximum power (kW) |
| `excludeDamaged` | boolean | Exclude damaged vehicles |
| `onlyDamaged` | boolean | Only damaged vehicles |
| `exteriorColors` | array | Exterior colour(s) |
| `sellerType` | string | Seller type |
| `priceRatings` | array | Price rating |
| `onlineSinceDays` | string | Listed within |
| `vatReclaimable` | boolean | VAT reclaimable only |
| `minSeats` | integer | Minimum seats |
| `doors` | string | Doors |
| `maxPreviousOwners` | integer | Maximum previous owners |
| `driveType` | string | Drive type |
| `emissionClass` | string | Emission class |
| `minSellerRating` | integer | Minimum seller rating |
| `keyword` | string | Keyword in description |
| `sortBy` | string | Sort order |
| `urls` | array | URLs (URL mode only) |
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
| `category` | string |
| `price` | integer |
| `priceFormatted` | string |
| `currency` | string |
| `firstRegistration` | string |
| `mileageKm` | integer |
| `powerKw` | integer |
| `powerHp` | integer |
| `fuel` | string |
| `transmission` | string |
| `city` | string |
| `zip` | string |
| `country` | string |
| `numImages` | integer |
| `previewImage` | string |
| `images` | list |
| `sponsored` | boolean |
| `sellerName` | string |
| `sellerCity` | string |
| `sellerCountry` | string |
| `rating` | float |
| `reviewCount` | integer |
| `description` | null |
| `features` | list |
| `attributes` | object |
| `relativeUrl` | string |
| `subTitle` | null |
| `listingType` | string |
| `priceRating` | string |
| `priceRatingLabel` | string |
| `vatDeductible` | boolean |
| `accidentFree` | null |
| `damageCondition` | null |
| `highlights` | list |

---

[← All scrapers](../../README.md)
