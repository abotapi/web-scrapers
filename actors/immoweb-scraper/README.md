# Immoweb.be Scraper

Extract property listings from immoweb.be. Get price, location, coordinates, images, and 27 structured fields per listing. Enable detail page fetching for 70+ additional fields, including description, EPC score, building details, energy features, and agent contact.

**[Open Immoweb.be Scraper on Apify](https://apify.com/abotapi/immoweb-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~immoweb-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "transactionType": "for-sale", "countries": ["BE"], "orderBy": "newest", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `transactionType` | string | Transaction Type (Search mode) |
| `propertyTypes` | array | Property Types |
| `postalCodes` | array | Postal Codes |
| `countries` | array | Countries |
| `orderBy` | string | Sort Order |
| `priceMin` | integer | Minimum Price (EUR) |
| `priceMax` | integer | Maximum Price (EUR) |
| `bedroomsMin` | integer | Minimum Bedrooms |
| `bedroomsMax` | integer | Maximum Bedrooms |
| `livingAreaMin` | integer | Minimum Living Area (m²) |
| `livingAreaMax` | integer | Maximum Living Area (m²) |
| `landAreaMin` | integer | Minimum Land Area (m²) |
| `landAreaMax` | integer | Maximum Land Area (m²) |
| `constructionYearMin` | integer | Minimum Construction Year |
| `buildingConditions` | array | Building Condition |
| `epcGradeMax` | string | Maximum EPC Grade |
| `hasGarden` | boolean | Has Garden |
| `hasTerrace` | boolean | Has Terrace |
| `hasSwimmingPool` | boolean | Has Swimming Pool |
| `newBuildsOnly` | boolean | New Builds Only |
| `urls` | array | Search URLs (URL mode) |
| `fetchDetails` | boolean | Fetch Detail Pages (applies to both mo |
| `maxItems` | integer | Maximum Listings |
| `maxPagesPerUrl` | integer | Maximum Pages per URL |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/immoweb-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `url` | string |
| `title` | string |
| `transactionType` | string |
| `propertyType` | string |
| `propertySubtype` | string |
| `price` | integer |
| `displayPrice` | string |
| `price_per_sqm` | integer |
| `bedrooms` | integer |
| `livingArea` | integer |
| `landArea` | integer |
| `street` | string |
| `number` | string |
| `postalCode` | string |
| `locality` | string |
| `district` | string |
| `province` | string |
| `region` | string |
| `regionCode` | string |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `images` | list |
| `imageCount` | integer |
| `salePrice` | integer |
| `lastModified` | string |
| `listingFlag` | string |
| `customerName` | string |

---

[← All scrapers](../../README.md)
