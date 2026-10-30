# REWE.de Scraper

Scrape REWE Germany (rewe.de) grocery products: current price, was-price and discount when genuinely on offer, brand, category, price per unit, images and tags. Prices match a real postal code you choose. Search keywords or paste product/listing links.

**[Open REWE.de Scraper on Apify](https://apify.com/abotapi/rewe-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rewe-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "zipCode": "50667", "searchTerm": "milch", "sortBy": "RELEVANCE_DESC", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `zipCode` * | string | Postal code (PLZ) |
| `searchTerm` | string | Search keyword |
| `categorySlug` | string | Category slug |
| `urls` | array | URLs to scrape |
| `brand` | string | Brand |
| `attribute` | string | Dietary / sourcing filter |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `sortBy` | string | Sort by |
| `campaignsOnly` | boolean | Offers only |
| `inStockOnly` | boolean | Available products only |
| `marketId` | string | REWE market id (advanced) |
| `searchTerms` | array | More search keywords |
| `productIds` | array | Shopping list product ids |
| `quantities` | array | Shopping list quantities |
| `fetchDetails` | boolean | Fetch product detail |
| `compact` | boolean | Compact output |
| `excludeEmptyFields` | boolean | Exclude empty fields |
| `descriptionMaxLength` | integer | Description max length |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rewe-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `tags` | list |
| `url` | string |
| `hasVariants` | boolean |
| `freeShipping` | boolean |
| `categoryId` | string |
| `category` | string |
| `categoryPath` | list |
| `image` | string |
| `images` | list |
| `price` | float |
| `currency` | string |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `pricePerUnit` | null |
| `grammage` | string |
| `available` | boolean |
| `offerValidTo` | null |
| `merchant` | string |
| `gtin` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
