# Properstar Scraper

Extract property listings from Properstar across global domains like .com, .co.uk, .ch, and .fr. Use search pages, listing URLs, or agency pages. Returns prices, multilingual descriptions, photos, floor plans, GPS coordinates, and agency details via Properstar’s data service.

**[Open Properstar Scraper on Apify](https://apify.com/abotapi/properstar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~properstar-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"startUrls": ["https://www.properstar.co.uk/united-kingdom/london/buy/apartment-house"], "transactionType": "any", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `startUrls` * | array | Properstar URLs |
| `transactionType` | string | Transaction type |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `luxuryOnly` | boolean | Luxury listings only |
| `enrichDetail` | boolean | Fetch full detail (amenities, views, y |
| `maxItems` | integer | Max listings |
| `maxPagesPerUrl` | integer | Max pages per URL |
| `maxResidentialMb` | integer | Residential traffic budget (MB) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/properstar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `class` | string |
| `transactionType` | string |
| `type` | string |
| `subType` | string |
| `title` | string |
| `automaticTitle` | string |
| `description` | string |
| `titleByLanguage` | object |
| `descriptionByLanguage` | object |
| `status` | string |
| `energyRating` | null |
| `co2Rating` | null |
| `ratings` | null |
| `geoPointReliable` | boolean |
| `price` | integer |
| `currency` | string |
| `priceValues` | list |
| `livingAreaSqm` | float |
| `landAreaSqm` | null |
| `livingAreaSqft` | float |
| `landAreaSqft` | null |
| `rooms` | integer |
| `bedrooms` | integer |
| `bathrooms` | null |
| `floor` | null |
| `constructionYear` | null |
| `address` | string |
| `city` | string |
| `postcode` | string |
| `countryISO` | string |
| `latitude` | float |
| `longitude` | float |
| `showAddress` | boolean |
| `geocodeLevel` | string |
| `pictures` | list |
| `picturesCount` | integer |
| `floorPlans` | list |
| `floorPlansCount` | null |

---

[← All scrapers](../../README.md)
