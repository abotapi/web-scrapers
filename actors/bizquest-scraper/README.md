# BizQuest Scraper

Extract business-for-sale, franchise, and asset listings from BizQuest. Search by category, US state, asking price, or use BizQuest URLs. Returns 50+ fields, including asking price, location, photos, broker name and phone where available, ready for CRM, deal pipeline, or spreadsheet use.

**[Open BizQuest Scraper on Apify](https://apify.com/abotapi/bizquest-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bizquest-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Florida"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `category` | string | Category |
| `locations` | array | Locations (US states) |
| `keyword` | string | Keyword |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Min asking price (USD) |
| `maxPrice` | integer | Max asking price (USD) |
| `urls` | array | BizQuest URLs |
| `includeDetails` | boolean | Fetch full listing details |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bizquest-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `listNumber` | integer |
| `title` | string |
| `url` | string |
| `description` | string |
| `image` | string |
| `images` | list |
| `askingPrice` | integer |
| `cashFlow` | null |
| `ebitda` | null |
| `leaseRateDuration` | integer |
| `leaseRatePerSquareFoot` | null |
| `realEstateIncludedInAskingPrice` | boolean |
| `financingTypeId` | integer |
| `initialFee` | null |
| `initialCapital` | null |
| `location` | string |
| `region` | string |
| `stateName` | string |
| `regionId` | integer |
| `locationCrumbs` | list |
| `category` | string |
| `categoryId` | integer |
| `listingTypeId` | integer |
| `isFranchise` | boolean |
| `categoryDetails` | null |
| `brokerName` | string |
| `brokerCompany` | string |
| `brokerPhone` | string |
| `tpnPhone` | string |
| `tpnPhoneExt` | string |
| `brokerPhoto` | string |
| `brokerProfileUrl` | string |
| `brokerCertifications` | null |
| `contactInfo` | object |
| `hotProperty` | boolean |
| `recentlyAdded` | boolean |
| `recentlyUpdated` | boolean |
| `listingPriceReduced` | boolean |
| `adLevelId` | integer |

---

[← All scrapers](../../README.md)
