# Yellow Pages AU Scraper

Scrape business listings from Yellow Pages Australia by type and location. Get names, contacts, websites, ratings, social links, and more. Supports filters, sorting, and custom output fields. Perfect for lead gen, local SEO, and market research.

**[Open Yellow Pages AU Scraper on Apify](https://apify.com/abotapi/yellow-pages-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yellow-pages-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "keyword", "businessType": "electrician", "location": "Melbourne, VIC", "limit": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `businessType` | string | Business type (Keyword mode) |
| `location` | string | Location (Keyword mode) |
| `urls` | array | Search URLs (URL mode) |
| `limit` | integer | Result limit |
| `pageNumber` | integer | Starting page number (Keyword mode onl |
| `fetchDetails` | boolean | Fetch details  reviews (enrichment) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yellow-pages-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `name` | string |
| `address` | string |
| `phone` | string |
| `email` | string |
| `website` | string |
| `scrapedFromPage` | integer |
| `primaryCategoryName` | string |
| `categoryText` | string |
| `detailsPageUrl` | string |
| `logoUrl` | string |
| `openingHoursToday` | string |
| `openingHoursDetails` | object |
| `openingHoursStructured` | list |
| `rating` | string |
| `reviewCount` | integer |
| `longDescription` | string |
| `slogan` | string |
| `isAd` | boolean |
| `hasPhotos` | boolean |
| `features` | string |
| `yearsInBusiness` | string |
| `yearsWithYellowPages` | string |
| `servingArea` | string |
| `listingType` | string |
| `claimedStatus` | string |
| `addressDetails` | object |
| `latitude` | float |
| `longitude` | float |

---

[← All scrapers](../../README.md)
