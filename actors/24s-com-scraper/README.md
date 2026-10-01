# 24S Scraper

Scrape 24S luxury fashion by category, filters, or URL. Extract brand, name, price, discounts, size stock, colors, images, descriptions, composition, and country of origin. Filter by brand, color, size, price, and sale.

**[Open 24S Scraper on Apify](https://apify.com/abotapi/24s-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~24s-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locale": "en-gb", "categories": ["women/shoes"], "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locale` | string | Market / locale |
| `categories` | array | Categories |
| `brands` | array | Brands |
| `colors` | array | Colors |
| `sizes` | array | Sizes |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `discounts` | array | On sale (min discount %) |
| `specialsOnly` | boolean | Specials only |
| `sortBy` | string | Sort by |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per category |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/24s-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `shortSku` | string |
| `model` | string |
| `name` | string |
| `title` | string |
| `brand` | string |
| `color` | string |
| `price` | integer |
| `discountPrice` | null |
| `currentPrice` | integer |
| `discountPercentage` | null |
| `currency` | string |
| `onSale` | boolean |
| `isOnSpecial` | boolean |
| `wasPrice` | null |
| `savingsAmount` | null |
| `discountPercent` | null |
| `promoEventName` | null |
| `discountStartDate` | null |
| `discountEndDate` | null |
| `inStock` | boolean |
| `stockLevel` | integer |
| `replenishment` | boolean |
| `exclusive` | boolean |
| `sizes` | list |
| `skus` | list |
| `otherColors` | list |
| `images` | list |
| `imagesCount` | integer |
| `productSlug` | string |
| `url` | string |
| `locale` | string |

---

[← All scrapers](../../README.md)
