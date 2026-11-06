# eMAG Scraper

Scrape eMAG products across Romania, Hungary, Bulgaria and Poland by keyword or URL. Extract product names, prices, discounts, sellers and stock availability. Optional enrichment adds descriptions, specifications and customer ratings.

**[Open eMAG Scraper on Apify](https://apify.com/abotapi/emag-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~emag-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["telefon"], "store": "ro", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "maxReviews": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Store URLs |
| `store` | string | Store |
| `sortBy` | string | Sort the store's results by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `onSaleOnly` | boolean | Discounted rows only |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `maxReviews` | integer | Max reviews per product |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/emag-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `store` | string |
| `pnk` | string |
| `productId` | string |
| `offerId` | string |
| `url` | string |
| `title` | string |
| `position` | integer |
| `searchTerm` | string |
| `categoryId` | string |
| `category` | string |
| `categoryTrail` | string |
| `price` | integer |
| `priceText` | string |
| `currency` | string |
| `originalPrice` | null |
| `onSale` | boolean |
| `discountPercent` | null |
| `brand` | null |
| `imageUrl` | string |
| `hasGenius` | boolean |
| `isMarketplace` | boolean |
| `description` | null |
| `manufacturer` | null |
| `sku` | null |
| `mpn` | null |
| `ean` | null |
| `itemCondition` | null |
| `keywords` | list |
| `badges` | list |
| `breadcrumbUrls` | list |
| `imageUrls` | list |
| `inStock` | null |
| `sellerName` | null |
| `sellerId` | null |
| `sellerSef` | null |
| `sellerRating` | null |
| `sellerPositiveShare` | null |
| `vendorType` | null |

---

[← All scrapers](../../README.md)
