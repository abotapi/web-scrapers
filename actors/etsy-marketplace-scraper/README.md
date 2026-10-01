# Etsy Scraper

Scrape Etsy listings by keyword, category, or URL. Extract titles, shops, prices, discounts, availability, images, categories, and variations. Optional detail mode adds descriptions, materials, shipping origin, and item-level reviews. Supports incremental monitoring.

**[Open Etsy Scraper on Apify](https://apify.com/abotapi/etsy-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~etsy-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["handmade necklace"], "sortBy": "most_relevant", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categoryPath` | string | Category path (optional) |
| `urls` | array | Etsy links |
| `sortBy` | string | Sort by |
| `onSaleOnly` | boolean | On sale only |
| `freeShippingOnly` | boolean | Free shipping only |
| `personalizableOnly` | boolean | Personalizable only |
| `minPrice` | integer | Minimum price (USD) |
| `maxPrice` | integer | Maximum price (USD) |
| `shipToCountry` | string | Ships to (country code, optional) |
| `fetchDetails` | boolean | Fetch listing details |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max pages per keyword / link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/etsy-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `title` | string |
| `url` | string |
| `shopId` | string |
| `shopName` | string |
| `shopUrl` | string |
| `categoryPath` | list |
| `price` | float |
| `currency` | string |
| `originalPrice` | integer |
| `discountPercentage` | integer |
| `onSale` | boolean |
| `availability` | string |
| `quantityAvailable` | integer |
| `images` | list |
| `videoUrl` | string |
| `description` | string |
| `materials` | list |
| `shippingOrigin` | object |
| `rating` | integer |
| `reviewCount` | integer |
| `ratingBreakdown` | object |
| `reviews` | list |
| `variations` | list |
| `searchMode` | string |

---

[← All scrapers](../../README.md)
