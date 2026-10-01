# Lennar Homes Scraper

Scrape Lennar new-home communities, move-in-ready homes and floor plans. Extract prices, monthly payment breakdowns, price drops, beds, baths, square footage, coordinates, amenities, virtual tours and 50+ fields. Search by state or paste Lennar URLs.

**[Open Lennar Homes Scraper on Apify](https://apify.com/abotapi/lennar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lennar-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "states": ["Florida"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `states` | array | States |
| `startUrls` | array | URLs |
| `includeCommunities` | boolean | Include communities |
| `includeHomesites` | boolean | Include move-in-ready homes |
| `enrichDetails` | boolean | Include floor plans (detail crawl) |
| `maxItems` | integer | Max records |
| `proxy` | object | Proxy |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lennar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `resultKind` | string |
| `id` | string |
| `state` | string |
| `stateCode` | string |
| `communityName` | string |
| `status` | string |
| `badge` | string |
| `brand` | string |
| `overview` | string |
| `url` | string |
| `imageUrl` | string |
| `city` | string |
| `market` | string |
| `priceLabel` | string |
| `priceFrom` | string |
| `basePrice` | null |
| `bedRange` | string |
| `bathRange` | string |
| `sqftRange` | string |
| `address` | null |
| `zipCode` | null |
| `latitude` | float |
| `longitude` | float |
| `googlePlaceId` | string |
| `propertyTypes` | null |
| `divisionNumber` | null |
| `communityNumber` | null |
| `mpcId` | integer |
| `mapBounds` | null |
| `subCommunityCount` | integer |
| `subCommunities` | list |
| `raw` | object |

---

[← All scrapers](../../README.md)
