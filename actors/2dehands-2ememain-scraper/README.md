# 2dehands & 2ememain Scraper

Scrape classifieds from 2dehands.be and 2ememain.be by keyword, filters, or URLs. Returns title, price, location, images, seller details, category, and full tag-based seller reviews. Supports sort, category, price filters, listing URLs, and search URLs.

**[Open 2dehands & 2ememain Scraper on Apify](https://apify.com/abotapi/2dehands-2ememain-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~2dehands-2ememain-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["bmw"], "domain": "2dehands.be", "sort": "optimized", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "BE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `queries` | array | Search keywords |
| `startUrls` | array | Listing or search URLs |
| `domain` | string | Site |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `sort` | string | Sort results |
| `categoryId` | integer | Category ID (optional) |
| `fetchDetails` | boolean | Fetch full listing details |
| `includeReviews` | boolean | Include seller reviews |
| `maxReviews` | integer | Max reviews per listing |
| `maxItems` | integer | Max listings (the run cap) |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/2dehands-2ememain-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `sourceSite` | string |
| `itemId` | string |
| `id` | string |
| `title` | string |
| `description` | string |
| `categorySpecificDescription` | string |
| `thinContent` | boolean |
| `price` | integer |
| `priceCents` | integer |
| `priceType` | string |
| `city` | string |
| `countryName` | string |
| `countryAbbreviation` | string |
| `latitude` | float |
| `longitude` | float |
| `distanceMeters` | integer |
| `location` | string |
| `date` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `pictures` | list |
| `sellerId` | integer |
| `sellerName` | string |
| `sellerVerified` | boolean |
| `sellerWebsiteUrl` | boolean |
| `sellerInformation` | object |
| `categoryId` | integer |
| `priorityProduct` | string |
| `videoOnVip` | boolean |
| `urgencyFeatureActive` | boolean |
| `napAvailable` | boolean |
| `reserved` | boolean |
| `extendedAttributes` | list |
| `traits` | list |
| `verticals` | list |
| `vipUrl` | string |
| `url` | string |
| `seedValue` | string |
| `pageOffset` | integer |

---

[← All scrapers](../../README.md)
