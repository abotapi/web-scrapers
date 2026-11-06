# Dun & Bradstreet Scraper

Scrape Dun & Bradstreet (dnb.com) business directory by company name, country, size, role or industry. Extract company profiles, revenue, employee counts, key executives, principals, contact details and stock information. Ideal for B2B lead generation, company research and market intelligence.

**[Open Dun & Bradstreet Scraper on Apify](https://apify.com/abotapi/dnb-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dnb-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["software"], "country": "us", "companyRole": "any", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Company name keywords |
| `country` | string | Country |
| `employeesMin` | integer | Minimum employees |
| `employeesMax` | integer | Maximum employees |
| `companyRole` | string | Company role |
| `urls` | array | Directory links |
| `fetchDetails` | boolean | Enrich company details |
| `maxPages` | integer | Max pages per scope |
| `maxItems` | integer | Max records |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dnb-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `companyName` | string |
| `encryptedDuns` | string |
| `profileUrl` | string |
| `url` | string |
| `companyRole` | string |
| `industryName` | string |
| `scopeKind` | string |
| `scope` | string |
| `searchQuery` | string |
| `position` | integer |
| `scrapedAt` | string |
| `addressStreet` | string |
| `addressPostalCode` | string |
| `addressCountry` | string |
| `employeesConsolidatedValue` | integer |
| `employeesConsolidatedScope` | string |
| `employeesConsolidatedReliability` | string |
| `employeesThisSiteValue` | integer |
| `employeesThisSiteScope` | string |
| `employeesThisSiteReliability` | string |
| `revenueFormatted` | string |
| `sales` | integer |
| `revenueReliability` | string |
| `revenueYear` | string |
| `salesCurrency` | string |
| `fiscalPeriodEnd` | string |
| `annualRevenues` | list |
| `financialHistory` | list |
| `keyPrincipal` | string |
| `principals` | list |
| `keyPrincipalPosition` | string |
| `totalPrincipals` | integer |
| `totalContactsOnFile` | string |
| `phone` | string |
| `website` | string |
| `stockExchange` | string |
| `stockTicker` | string |
| `tradeStyleName` | string |
| `industries` | list |

---

[← All scrapers](../../README.md)
