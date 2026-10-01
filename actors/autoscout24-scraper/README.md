# AutoScout24 Scraper

A lean, production-grade scraper for autoscout24.com. Point it at a search, get back clean JSON with 30+ fields per vehicle. Designed for dealers, market analysts, valuation pipelines, lead generation, and anyone who needs autoscout24 data on tap.

**[Open AutoScout24 Scraper on Apify](https://apify.com/abotapi/autoscout24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~autoscout24-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "ustate": "both", "sortBy": "standard", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `urls` | array | URLs (URL mode only) |
| `make` | string | Make |
| `model` | string | Model |
| `countries` | array | Countries |
| `ustate` | string | Vehicle state |
| `bodyType` | string | Body type |
| `fuelTypes` | array | Fuel type(s) |
| `transmission` | string | Transmission |
| `priceMin` | integer | Minimum price (EUR) |
| `priceMax` | integer | Maximum price (EUR) |
| `yearMin` | integer | Minimum first registration year |
| `yearMax` | integer | Maximum first registration year |
| `kmMin` | integer | Minimum mileage (km) |
| `kmMax` | integer | Maximum mileage (km) |
| `powerMinKw` | integer | Minimum power (kW) |
| `powerMaxKw` | integer | Maximum power (kW) |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch full details |
| `fetchDealerInfo` | boolean | Fetch dealer email, VAT, address (from |
| `maxListings` | integer | Maximum listings |
| `maxPages` | integer | Maximum pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/autoscout24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `make` | string |
| `model` | string |
| `modelGroup` | string |
| `variant` | string |
| `modelVersion` | string |
| `year` | integer |
| `firstRegistration` | string |
| `bodyType` | string |
| `transmission` | string |
| `fuel` | string |
| `engineDisplacement` | string |
| `powerKw` | integer |
| `powerHp` | integer |
| `mileageKm` | integer |
| `mileageDisplay` | string |
| `price` | integer |
| `priceDisplay` | string |
| `currency` | string |
| `isVatLabelLegallyRequired` | boolean |
| `isOfferNew` | boolean |
| `offerType` | string |
| `vehicleType` | string |
| `isDeliverable` | null |
| `country` | string |
| `city` | string |
| `zip` | string |
| `street` | string |
| `sellerType` | string |
| `sellerId` | string |
| `companyName` | string |
| `contactName` | string |
| `phones` | list |
| `ratingsCount` | integer |
| `ratingsStars` | float |
| `whatsappNumber` | string |
| `dealerLogoUrl` | string |
| `dealerInfoPageUrl` | string |

---

[← All scrapers](../../README.md)
