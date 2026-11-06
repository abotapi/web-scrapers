# Curtsy Fashion Resale Scraper

Scrape Curtsy, the US secondhand fashion marketplace: listings with brand, size, list vs original retail price, condition, photos and seller profile. Keyword and brand search, category browse, item and closet links, seller reviews, incremental monitoring, resume, MCP export.

**[Open Curtsy Fashion Resale Scraper on Apify](https://apify.com/abotapi/curtsy-app-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~curtsy-app-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Keyword search (optional) |
| `brand` | string | Brand (optional) |
| `category` | string | Category (optional) |
| `startUrls` | array | Item, closet or collection links |
| `urls` | array | Links (alias) |
| `priceMin` | integer | Min price (USD, optional) |
| `priceMax` | integer | Max price (USD, optional) |
| `color` | string | Color (optional) |
| `freeShippingOnly` | boolean | Free shipping only |
| `nwtOnly` | boolean | New with tags only |
| `fetchDetails` | boolean | Read listing details |
| `fetchReviews` | boolean | Collect seller reviews and comments |
| `maxReviews` | integer | Max reviews per listing |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope (0  no cap) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/curtsy-app-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `title` | string |
| `url` | string |
| `detailUrl` | string |
| `route` | string |
| `brand` | string |
| `brandId` | string |
| `price` | integer |
| `retailPrice` | null |
| `suggestedPrice` | integer |
| `priceWithFees` | float |
| `shippingPrice` | integer |
| `shippingCost` | float |
| `size` | string |
| `sizeCategory` | string |
| `category` | string |
| `color` | string |
| `condition` | string |
| `isNWT` | boolean |
| `sold` | boolean |
| `loves` | integer |
| `numImages` | integer |
| `imageUrl` | string |
| `imageUrls` | list |
| `thumbW` | integer |
| `thumbH` | integer |
| `thumbColor` | string |
| `isSteal` | boolean |
| `hot` | boolean |
| `isNew` | boolean |
| `justListed` | boolean |
| `freeShipping` | boolean |
| `postedAt` | string |
| `firstApprovedAt` | string |
| `postedAgo` | string |
| `feedVisible` | boolean |
| `sellerId` | string |
| `sellerName` | string |
| `scope` | string |
| `titleClean` | string |

---

[← All scrapers](../../README.md)
