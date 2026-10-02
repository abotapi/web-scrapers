# Homely.com.au Scraper

Scrape Homely.com.au properties for sale, rent, and sold, plus agent finder, suburb reviews, ratings, and Q&A. Search by suburb or use URLs. Returns 50+ fields, including price, beds, baths, parking, geo, agent contacts, photos, and inspections.

**[Open Homely.com.au Scraper on Apify](https://apify.com/abotapi/homely-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~homely-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "dataset": "buy", "location": "Bondi NSW 2026", "agentSpecialty": "any", "sort": "default", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. How will you supply the input |
| `dataset` | string | 2. What do you want to scrape |
| `location` | string | Location (suburb) |
| `locationIds` | array | Location IDs (advanced) |
| `agentSpecialty` | string | Agent specialty |
| `officeId` | integer | Office ID (advanced) |
| `sort` | string | Sort agents by |
| `startUrls` | array | Homely URLs |
| `priceMin` | integer | Min price |
| `priceMax` | integer | Max price |
| `bedroomsMin` | integer | Min bedrooms |
| `bedroomsMax` | integer | Max bedrooms |
| `bathroomsMin` | integer | Min bathrooms |
| `carSpacesMin` | integer | Min car spaces |
| `propertyTypes` | array | Property types |
| `propertyFeatures` | array | Required features |
| `isUnderOffer` | boolean | Under offer only |
| `detail` | boolean | Fetch full details (richer records) |
| `includeSuburbInsights` | boolean | Add suburb insights to each listing |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per location |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/homely-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `mode` | string |
| `id` | integer |
| `uri` | string |
| `url` | string |
| `title` | string |
| `statusType` | string |
| `listingType` | string |
| `propertyType` | string |
| `tierType` | string |
| `isExclusiveList` | boolean |
| `isUnderOffer` | boolean |
| `daysOnMarket` | string |
| `daysOnHomely` | integer |
| `isNew` | boolean |
| `price` | object |
| `priceValue` | integer |
| `address` | object |
| `location` | object |
| `features` | object |
| `featureTags` | list |
| `agents` | list |
| `office` | object |
| `images` | list |
| `videos` | list |
| `externalLinks` | list |
| `inspections` | list |
| `auction` | object |
| `landFeatures` | null |
| `slugs` | object |
| `nextInspection` | string |
| `soldOn` | null |
| `soldPrice` | string |
| `soldPriceValue` | null |
| `auctionOn` | string |
| `loanPriceEstimate` | integer |
| `sourceUrl` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
