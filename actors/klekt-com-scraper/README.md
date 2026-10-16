# KLEKT Sneaker & Apparel Resale Scraper

Scrape sneaker and streetwear listings from KLEKT (klekt.com). Browse the catalog with filters and extract product details, prices, and availability for resale market research and price monitoring.

**[Open KLEKT Sneaker & Apparel Resale Scraper on Apify](https://apify.com/abotapi/klekt-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~klekt-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "browse", "strategy": "trending", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Scrape mode |
| `productUrls` | array | Product URLs |
| `strategy` | string | Catalogue section |
| `brand` | string | Brand |
| `brandLine` | string | Brand line / model family |
| `productCategory` | string | Product category |
| `sizeCategory` | string | Size category |
| `sizeMetric` | string | Size system (needed for Size) |
| `size` | string | Size (needs Size system) |
| `boxCondition` | string | Box condition |
| `listingType` | string | Listing type (Used section only) |
| `availability` | string | Availability |
| `priceFrom` | integer | Minimum price (EUR) |
| `priceTo` | integer | Maximum price (EUR) |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max catalogue pages (Browse mode) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/klekt-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `type` | string |
| `name` | string |
| `sku` | string |
| `slug` | string |
| `colorway` | string |
| `description` | string |
| `availability` | string |
| `priceAmount` | integer |
| `lastSoldPrice` | integer |
| `priceCurrency` | string |
| `imageUrl` | string |
| `url` | string |
| `brand` | string |
| `seller` | string |
| `images` | list |
| `model` | string |
| `lowestListingPrice` | integer |
| `lowestListingSize` | string |
| `detailScraped` | boolean |

---

[← All scrapers](../../README.md)
