# Flippa Scraper

Scrape Flippa listings with full enrichment, including revenue, profit, valuation multiples, traffic, business age, location, monetization, badges and more. Search with filters or URLs, with concurrent enrichment for fast, low-resource runs.

**[Open Flippa Scraper on Apify](https://apify.com/abotapi/flippa-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~flippa-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "status": ["open"], "propertyTypes": ["ai_apps_and_tools"], "sortBy": "most_relevant", "revenueGenerating": "any", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search Mode |
| `status` | array | Listing Status |
| `propertyTypes` | array | Asset Types |
| `siteTypes` | array | Site Types |
| `saleMethods` | array | Sale Methods |
| `sortBy` | string | Sort By |
| `minPrice` | integer | Min Price (USD) |
| `maxPrice` | integer | Max Price (USD) |
| `minMonthlyProfit` | integer | Min Monthly Profit (USD) |
| `maxMonthlyProfit` | integer | Max Monthly Profit (USD) |
| `minMonthlyRevenue` | integer | Min Monthly Revenue (USD) |
| `maxMonthlyRevenue` | integer | Max Monthly Revenue (USD) |
| `minUniquesPerMonth` | integer | Min Uniques per Month |
| `minAgeMonths` | integer | Min Age (months) |
| `maxAgeMonths` | integer | Max Age (months) |
| `tlds` | array | Domain Extensions (TLD) |
| `sellerLocation` | string | Seller Location |
| `verifiedRevenueOnly` | boolean | Verified Revenue Only |
| `verifiedTrafficOnly` | boolean | Verified Traffic Only |
| `manuallyVettedOnly` | boolean | Manually Vetted Only |
| `editorsChoiceOnly` | boolean | Editor's Choice Only |
| `superSellerOnly` | boolean | Super Seller Only |
| `brokerSellerOnly` | boolean | Brokered Listings Only |
| `sponsoredOnly` | boolean | Sponsored Only |
| `buyItNowOnly` | boolean | Buy It Now Only |
| `reserveMetOnly` | boolean | Reserve Met Only |
| `priceDroppedOnly` | boolean | Price Reduced Only |
| `managedByFlippaOnly` | boolean | Managed by Flippa Only |
| `earlyAccessOnly` | boolean | First Access Only |
| `revenueGenerating` | string | Revenue Generating |
| `urls` | array | Direct URLs |
| `fetchDetails` | boolean | Fetch Detail Data |
| `maxListings` | integer | Max Listings |
| `maxPages` | integer | Max Pages per Search |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/flippa-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `summary` | string |
| `propertyName` | null |
| `propertyType` | null |
| `siteType` | null |
| `category` | string |
| `monetization` | null |
| `primaryPlatform` | null |
| `saleMethod` | string |
| `saleMethodTitle` | string |
| `status` | null |
| `endAt` | null |
| `price` | integer |
| `originalPrice` | integer |
| `priceText` | string |
| `originalPriceText` | string |
| `priceDropped` | boolean |
| `priceDroppedPercent` | integer |
| `underOffer` | null |
| `currency` | string |
| `currencyLabel` | string |
| `targetRaiseAmount` | null |
| `targetRaiseAmountText` | null |
| `ttmRevenue` | null |
| `monthlyProfit` | integer |
| `monthlyRevenue` | integer |
| `annualProfit` | integer |
| `annualRevenue` | integer |
| `profitMultiple` | float |
| `revenueMultiple` | null |
| `hasMultiple` | null |
| `uniquesPerMonth` | null |
| `pageViewsPerMonth` | null |
| `annualOrganicTraffic` | null |
| `authorityScore` | null |
| `appRating` | null |
| `siteAge` | string |
| `ageInYears` | string |

---

[← All scrapers](../../README.md)
