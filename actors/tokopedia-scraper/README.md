# Tokopedia Scraper

Extract product data from Tokopedia, Indonesia’s largest marketplace. Search by keyword with sorting and filters, or use product/result URLs. Returns price, discount, rating, sold count, seller, category, images, and optional details like description, videos, variants, and wholesale tiers.

**[Open Tokopedia Scraper on Apify](https://apify.com/abotapi/tokopedia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tokopedia-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["sepatu"], "sortBy": "relevance", "condition": "any", "shopTier": "any", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `urls` | array | Product or result URLs |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price (IDR) |
| `maxPrice` | integer | Maximum price (IDR) |
| `condition` | string | Condition |
| `minRating` | integer | Minimum rating |
| `shopTier` | string | Seller type |
| `freeShippingOnly` | boolean | Free shipping only |
| `discountOnly` | boolean | Discounted products only |
| `fetchDetails` | boolean | Fetch full product details |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |
| `maxNotifyItems` | integer | Max items to export |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tokopedia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `productIdOld` | integer |
| `ttsProductID` | string |
| `productKey` | string |
| `name` | string |
| `url` | string |
| `applink` | string |
| `condition` | null |
| `categoryId` | string |
| `categoryName` | string |
| `categoryBreadcrumb` | string |
| `categoryGaKey` | string |
| `minOrder` | null |
| `weight` | null |
| `weightUnit` | null |
| `description` | null |
| `etalase` | null |
| `price` | integer |
| `priceText` | string |
| `originalPrice` | null |
| `discountPercentage` | integer |
| `priceRange` | null |
| `wholesale` | list |
| `isOnSpecial` | boolean |
| `specialsCategory` | null |
| `specialsCampaignId` | null |
| `specialsDiscountPercentage` | null |
| `specialsOriginalPrice` | null |
| `specialsPrice` | null |
| `specialsStock` | null |
| `specialsOriginalStock` | null |
| `specialsStockSoldPercentage` | null |
| `specialsStartDate` | null |
| `specialsEndDate` | null |
| `specialsThematicName` | null |
| `cashbackPercentage` | null |
| `variantSkus` | list |
| `stock` | null |
| `stockText` | null |
| `isPreorder` | null |

---

[← All scrapers](../../README.md)
