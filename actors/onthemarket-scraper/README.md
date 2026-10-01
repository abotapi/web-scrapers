# OnTheMarket Scraper

Scrape onthemarket.com for-sale, to-rent and new-homes listings with 85+ fields: price, address & geo, bedrooms/bathrooms, full description, key info, nearest stations & schools, area stats, floorplans, virtual tours and complete agent contacts. Search by location + filters or paste URLs.

**[Open OnTheMarket Scraper on Apify](https://apify.com/abotapi/onthemarket-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~onthemarket-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "channel": "FOR-SALE", "locations": ["London"], "sortType": "recommended", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channel` | string | Channel |
| `locations` | array | Locations |
| `startUrls` | array | Start URLs |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `propertyTypes` | array | Property types |
| `radius` | string | Search radius (miles) |
| `sortType` | string | Sort order |
| `includeUnderOffer` | boolean | Include under offer / SSTC |
| `includeDetails` | boolean | Include full property details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/onthemarket-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `channel` | string |
| `propertyTitle` | string |
| `humanisedPropertyType` | string |
| `displayAddress` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `displayPrice` | string |
| `shortPrice` | string |
| `price` | integer |
| `priceQualifier` | string |
| `latitude` | float |
| `longitude` | float |
| `mainLabel` | string |
| `daysSinceAddedReduced` | string |
| `reduced` | null |
| `spotlight` | boolean |
| `matterportVirtualTour` | boolean |
| `features` | list |
| `images` | list |
| `coverImage` | string |
| `dataLabelId` | null |
| `agentId` | integer |
| `agentName` | string |
| `agentLogo` | string |
| `rawAgent` | object |
| `detailScraped` | boolean |

---

[← All scrapers](../../README.md)
