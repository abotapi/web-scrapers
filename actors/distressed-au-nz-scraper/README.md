# Distressed Property Scraper

Find mortgagee-sale and distressed-property listings in Australia and New Zealand. NZ results require a confirmed mortgagee-sale flag; AU results use keyword filtering. Get property, price, location and agent details, plus auction dates where available. Resume runs or track incremental changes

**[Open Distressed Property Scraper on Apify](https://apify.com/abotapi/distressed-au-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~distressed-au-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": ["nz"], "auListingType": "buy", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `country` | array | Country lanes |
| `urls` | array | URLs |
| `nzRegion` | string | NZ Region (optional) |
| `nzListingType` | string | NZ Listing pool (optional) |
| `auState` | string | AU State (optional) |
| `auListingType` | string | AU Listing type |
| `auPropertyType` | string | AU Property type (optional) |
| `auBedroomsMin` | integer | AU Min bedrooms (optional) |
| `auBedroomsMax` | integer | AU Max bedrooms (optional) |
| `auPriceMin` | integer | AU Min price AUD (optional) |
| `auPriceMax` | integer | AU Max price AUD (optional) |
| `auExcludes` | array | AU Exclude words (optional) |
| `fetchDetails` | boolean | Fetch detail pages |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search (0  unlimited) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/distressed-au-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `country` | string |
| `source` | string |
| `title` | string |
| `distressType` | string |
| `url` | string |
| `portalId` | string |
| `publishedAt` | string |
| `location` | object |
| `valueText` | string |
| `status` | string |
| `parties` | list |
| `description` | string |
| `attachments` | list |
| `details` | object |
| `raw` | object |

---

[← All scrapers](../../README.md)
