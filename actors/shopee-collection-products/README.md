# Shopee Cambodia Scraper

Scrape public Shopee Cambodia collections and campaign products without signing in. Extract prices, ratings, images, variants, seller information and other structured product details from public listings.

**[Open Shopee Cambodia Scraper on Apify](https://apify.com/abotapi/shopee-collection-products?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~shopee-collection-products/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Inputs


Full details on the [scraper page](https://apify.com/abotapi/shopee-collection-products?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `itemId` | string |
| `shopId` | string |
| `name` | string |
| `translatedName` | string |
| `url` | string |
| `price` | integer |
| `originalPrice` | null |
| `discountPercent` | integer |
| `currency` | string |
| `rating` | float |
| `ratingCount` | integer |
| `ratingDistribution` | list |
| `images` | list |
| `variants` | list |
| `videos` | list |
| `shop` | object |
| `categoryIds` | list |
| `brand` | null |
| `inStock` | boolean |
| `likes` | integer |
| `isVerifiedSeller` | boolean |
| `collectionId` | string |
| `collectionName` | null |
| `market` | string |
| `sourceUrl` | string |
| `scrapedAt` | string |
| `productData` | object |
| `displayAssets` | object |

---

[← All scrapers](../../README.md)
