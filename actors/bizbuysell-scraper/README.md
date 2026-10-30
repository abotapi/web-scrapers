# BizBuySell Scraper

Extract business-for-sale and franchise listings from bizbuysell.com with financials, full descriptions, photos, and broker contact details. Search by filters or paste BizBuySell URLs directly. Returns 30+ structured fields per listing, ready for CRMs, deal pipelines, or spreadsheets.

**[Open BizBuySell Scraper on Apify](https://apify.com/abotapi/bizbuysell-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bizbuysell-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listingType": "all", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `keyword` | string | Keyword |
| `category` | string | Category |
| `location` | string | Location |
| `listingType` | string | Listing type |
| `minAskingPrice` | integer | Min asking price (USD) |
| `maxAskingPrice` | integer | Max asking price (USD) |
| `minCashFlow` | integer | Min cash flow / SDE (USD) |
| `minGrossRevenue` | integer | Min gross revenue (USD) |
| `maxCashFlow` | integer | Max cash flow (USD) |
| `maxGrossRevenue` | integer | Max gross revenue (USD) |
| `sortBy` | string | Sort by |
| `urls` | array | BizBuySell URLs |
| `startUrls` | array | Start URLs (alias of BizBuySell URLs) |
| `fetchDetails` | boolean | Fetch full listing details |
| `maxPages` | integer | Max search pages |
| `max_pages` | integer | max_pages (alias of Max search pages) |
| `maxListings` | integer | Max listings |
| `results_wanted` | integer | results_wanted (alias of Max listings) |
| `proxy` | object | Proxy |
| `proxyConfiguration` | object | proxyConfiguration (alias of Proxy) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bizbuysell-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `category` | string |
| `listingType` | string |
| `city` | string |
| `state` | string |
| `shortDescription` | string |
| `fullDescription` | null |
| `askingPrice` | integer |
| `cashFlow` | null |
| `grossRevenue` | null |
| `ebitda` | null |
| `inventory` | null |
| `ffe` | null |
| `realEstate` | null |
| `establishedYear` | null |
| `employees` | null |
| `reasonForSelling` | null |
| `supportTraining` | null |
| `financingAvailable` | null |
| `relocatable` | null |
| `homeBased` | null |
| `franchise` | null |
| `leaseInfo` | null |
| `facilities` | null |
| `growthExpansion` | null |
| `competition` | null |
| `realEstateIncluded` | boolean |
| `priceReduced` | boolean |
| `imageUrl` | string |
| `images` | list |
| `brokerName` | string |
| `brokerPhone` | null |
| `brokerageName` | null |
| `brokerProfileUrl` | null |
| `brokerLicense` | null |
| `datePosted` | null |
| `isVerified` | null |
| `location` | string |

---

[← All scrapers](../../README.md)
