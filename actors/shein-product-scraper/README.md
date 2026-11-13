# SHEIN Scraper

Scrape SHEIN product listings by keyword or from any category, sale or search link. Returns product ID, SKU, title, link, category, current price, genuine was-price and discount, star rating, review count, stock, flash-sale and clearance flags, and images. Nine regional storefronts.

**[Open SHEIN Scraper on Apify](https://apify.com/abotapi/shein-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~shein-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"urls": ["https://au.shein.com/RecommendSelection/Women-Clothing-sc-017172961.html", "https://au.shein.com/RecommendSelection/Home-Kitchen-sc-017185546.html", "https://au.shein.com/pdsearch/summer%20dress/", "https://au.shein.com/Women-Dresses-c-1727.html"], "storefront": "au", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `urls` | array | Listing URLs |
| `searchTerms` | array | Search keywords |
| `storefront` | string | Storefront |
| `includeOutOfStock` | boolean | Include out-of-stock products |
| `sortBy` | string | Sort by |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `minRating` | number | Minimum rating |
| `onSaleOnly` | boolean | Discounted products only |
| `categories` | array | Categories |
| `maxItems` | integer | Maximum products |
| `maxPages` | integer | Maximum listing pages per URL |
| `enableLegacyBrowserLane` | boolean | Enable legacy browser lane |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/shein-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `spu` | string |
| `title` | string |
| `url` | string |
| `category` | string |
| `categoryId` | string |
| `price` | float |
| `originalPrice` | null |
| `discountPercent` | null |
| `discountAmount` | null |
| `isOnSale` | boolean |
| `currency` | string |
| `priceUsd` | float |
| `rating` | float |
| `reviewsCount` | integer |
| `inStock` | boolean |
| `stock` | integer |
| `isFlashSale` | boolean |
| `isClearance` | boolean |
| `hasVideo` | boolean |
| `storeCode` | string |
| `mallCode` | string |
| `image` | string |
| `images` | list |
| `scrapedAt` | string |
| `priceFormatted` | string |
| `originalPriceFormatted` | null |
| `currencyCode` | string |
| `country` | string |
| `estimatedPrice` | null |
| `reviewsCountText` | string |
| `fit` | object |
| `soldCountText` | string |
| `rankLabel` | string |
| `badges` | list |
| `dealEndsAt` | null |
| `promotions` | list |
| `quickShip` | boolean |
| `isCustomizable` | boolean |

---

[← All scrapers](../../README.md)
