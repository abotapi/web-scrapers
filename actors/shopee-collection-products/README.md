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
  -d '{"urls": ["https://shopeekh.com/collections/12453606", "https://shopeekh.com/collections/12453606?page=1", "https://shopeekh.com/m/Shopee-Beauty", "https://shopeekh.com/api/v4/microsite/get_products_for_collection_landing_page?by=relevancy&card_set_name=Microsite%20ATC%20Card&collection_id=12453606&item_order=0&limit=60&match_id=12453606&need_customised_item_card=true&newest=0&offset=0&order=desc", "https://shopeekh.com/api/v4/pagebuilder/get_csr_page?page_url=Shopee-Beauty&platform=4&timestamp=0"], "maxItems": 10, "maxPages": 1, "sortBy": "relevance", "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `urls` | array | Collection or campaign URLs |
| `maxItems` | integer | Maximum products |
| `maxPages` | integer | Maximum pages per collection |
| `sortBy` | string | Sort products by |
| `proxy` | object | Proxy configuration |

`*` required

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
| `originalPrice` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `rating` | float |
| `ratingCount` | integer |
| `ratingDistribution` | list |
| `images` | list |
| `variants` | list |
| `videos` | null |
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
| `priceMax` | integer |
| `isOnSale` | boolean |
| `historicalSoldEstimated` | null |
| `shopName` | string |
| `location` | string |
| `hasVariations` | boolean |
| `variationOptions` | list |

---

[← All scrapers](../../README.md)
