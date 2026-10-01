# eBay Scraper

Scrape eBay by keyword, category, seller or pasted link across 16 country storefronts. Returns id, title, condition, price, buying format, delivery, returns, seller feedback and more, with optional item specifics and full descriptions. Incremental mode tracks changes.

**[Open eBay Scraper on Apify](https://apify.com/abotapi/ebay-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ebay-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["laptop"], "marketplace": "com", "buyingFormat": "any", "itemLocation": "default", "sortBy": "best_match", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `sellerUsernames` | array | Sellers |
| `marketplace` | string | Marketplace |
| `categoryId` | string | Category id |
| `condition` | array | Condition |
| `buyingFormat` | string | Buying format |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `freeShippingOnly` | boolean | Free delivery only |
| `freeReturnsOnly` | boolean | Free returns only |
| `returnsAcceptedOnly` | boolean | Returns accepted only |
| `itemLocation` | string | Item location |
| `sortBy` | string | Sort by |
| `urls` | array | Marketplace links |
| `minSellerFeedbackPercent` | integer | Minimum seller feedback percentage |
| `fetchDetails` | boolean | Read item pages |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max result pages per keyword, seller o |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ebay-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `url` | string |
| `title` | string |
| `subtitle` | string |
| `condition` | string |
| `conditionId` | string |
| `brand` | null |
| `marketplace` | string |
| `price` | float |
| `priceMax` | null |
| `priceText` | string |
| `currency` | string |
| `originalPrice` | null |
| `discountPercent` | null |
| `listingType` | string |
| `bidCount` | null |
| `timeLeft` | null |
| `shippingCost` | null |
| `shippingText` | string |
| `freeShipping` | boolean |
| `itemLocation` | string |
| `returnsText` | string |
| `freeReturns` | boolean |
| `soldCount` | integer |
| `sellerName` | string |
| `sellerUrl` | string |
| `sellerFeedbackPercent` | float |
| `sellerFeedbackCount` | integer |
| `badges` | list |
| `imageUrl` | string |
| `attributes` | list |
| `pageNumber` | integer |
| `sourceUrl` | string |
| `images` | null |
| `itemSpecifics` | null |
| `categoryPath` | null |
| `paymentMethods` | null |
| `mpn` | null |
| `model` | null |
| `color` | null |

---

[← All scrapers](../../README.md)
