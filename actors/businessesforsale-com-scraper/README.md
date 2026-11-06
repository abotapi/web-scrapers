# BusinessesForSale.com Scraper

Extract businesses and franchises listed for sale on BusinessesForSale.com. Search by keywords, country, price, revenue, profit, sort, or use search/listing URLs. Returns title, asking price, revenue, cash flow, location, premises size, employees, photos, categories, and description.

**[Open BusinessesForSale.com Scraper on Apify](https://apify.com/abotapi/businessesforsale-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~businessesforsale-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": "restaurant", "country": "global", "sortBy": "Default", "pageSize": "50", "maxPages": 1, "maxListings": 10, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | string | Keywords |
| `country` | string | Country / market |
| `minPrice` | integer | Min asking price |
| `maxPrice` | integer | Max asking price |
| `minRevenue` | integer | Min revenue (turnover) |
| `maxRevenue` | integer | Max revenue (turnover) |
| `minProfit` | integer | Min cash flow (profit) |
| `maxProfit` | integer | Max cash flow (profit) |
| `priceDisclosedOnly` | boolean | Asking price disclosed only |
| `revenueDisclosedOnly` | boolean | Revenue disclosed only |
| `profitDisclosedOnly` | boolean | Cash flow disclosed only |
| `sortBy` | string | Sort by |
| `queryKeywords` | array | Multiple keyword searches |
| `querySort` | string | Sort (free text) |
| `queryStateOrRegion` | string | State / region |
| `queryCityOrArea` | string | City / area |
| `queryIndustrySlug` | string | Industry slug |
| `querySearchPath` | string | Custom search path |
| `queryMinAskingPrice` | string | Min asking price (10K / 1.5M) |
| `queryMaxAskingPrice` | string | Max asking price (10K / 1.5M) |
| `queryMinGrossIncome` | string | Min revenue (10K / 1.5M) |
| `queryMaxGrossIncome` | string | Max revenue (10K / 1.5M) |
| `queryMinCashFlow` | string | Min cash flow (10K / 1.5M) |
| `queryMaxCashFlow` | string | Max cash flow (10K / 1.5M) |
| `urls` | array | Listing or search URLs |
| `startUrls` | array | Start URLs (alias of URLs) |
| `fetchDetails` | boolean | Fetch listing details |
| `pageSize` | string | Results per page |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `maxItems` | integer | Max items (alias of Max listings) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/businessesforsale-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `listingClass` | string |
| `labels` | list |
| `searchCountry` | string |
| `locationText` | string |
| `locationDetail` | string |
| `country` | null |
| `region` | null |
| `locality` | null |
| `askingPriceDisplay` | string |
| `askingPriceValue` | integer |
| `priceCurrency` | string |
| `businessFunction` | null |
| `revenueDisplay` | string |
| `revenueValue` | integer |
| `cashFlowDisplay` | string |
| `cashFlowValue` | integer |
| `tenure` | null |
| `sizeSqFt` | null |
| `tradingHours` | string |
| `employees` | string |
| `yearsEstablished` | string |
| `description` | string |
| `categories` | list |
| `financials` | object |
| `details` | object |
| `seller` | null |
| `thumbnail` | string |
| `imageCount` | integer |
| `images` | list |
| `location` | string |
| `status` | string |
| `ebitda` | null |
| `ffne` | null |
| `inventoryValue` | null |
| `totalPhotos` | integer |
| `hasVideo` | boolean |

---

[← All scrapers](../../README.md)
