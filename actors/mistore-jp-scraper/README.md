# Isetan Mitsukoshi Scraper

Scrape the Isetan Mitsukoshi department store online shop (mistore.jp). Search by keyword or department, or paste search, department, brand and product links. Returns id, title, brand, category, JPY price, sale window, stock, colours and images, plus specifications, variants and customer reviews.

**[Open Isetan Mitsukoshi Scraper on Apify](https://apify.com/abotapi/mistore-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mistore-jp-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["バッグ"], "sortBy": "recommended", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyCountry": "JP"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categories` | array | Departments |
| `urls` | array | Store links or product ids |
| `sortBy` | string | Sort results by |
| `badges` | array | Only products with these badges |
| `colors` | array | Colour families |
| `brandCodes` | array | Brand codes |
| `minPrice` | integer | Minimum price (JPY) |
| `maxPrice` | integer | Maximum price (JPY) |
| `includeOutOfStock` | boolean | Include out of stock products |
| `fetchDetails` | boolean | Fetch full product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword, departme |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mistore-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `searchMode` | string |
| `scrapedAt` | string |
| `productId` | string |
| `title` | string |
| `brand` | string |
| `url` | string |
| `image` | string |
| `price` | integer |
| `priceMin` | integer |
| `priceMax` | integer |
| `currency` | string |
| `onSale` | boolean |
| `inStock` | boolean |
| `colorCodes` | list |
| `badgeCodes` | list |
| `saleStartsAt` | string |
| `saleEndsAt` | null |
| `cardholderOnly` | boolean |
| `digitalProduct` | null |
| `brandCode` | string |
| `brandUrl` | string |
| `sku` | string |
| `description` | string |
| `originalPrice` | null |
| `discountPercent` | null |
| `availability` | string |
| `stockNote` | null |
| `images` | list |
| `thumbnails` | list |
| `videos` | list |
| `variants` | list |
| `specifications` | list |
| `allergens` | list |
| `giftOptions` | list |
| `paymentMethods` | list |
| `badges` | list |
| `notices` | list |
| `breadcrumbs` | list |
| `categoryPath` | list |
| `topCategory` | string |

---

[← All scrapers](../../README.md)
