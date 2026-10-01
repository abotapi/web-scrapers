# Walgreens Products & Reviews Scraper

Scrape Walgreens products by keyword, category or product URL. Extract prices, promotions, availability, ingredients, descriptions, product details, ratings and customer reviews in clean, structured data.

**[Open Walgreens Products & Reviews Scraper on Apify](https://apify.com/abotapi/walgreens-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~walgreens-com/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["toothpaste"], "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "maxReviewsPerProduct": 10, "proxy": {"useApifyProxy": false}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search terms |
| `brands` | array | Brands |
| `productTypes` | array | Product types |
| `minPrice` | number | Minimum price (USD) |
| `maxPrice` | number | Maximum price (USD) |
| `minRating` | number | Minimum rating |
| `onlineOnly` | boolean | Available online only |
| `offersOnly` | boolean | Products with offers only |
| `sortBy` | string | Sort results |
| `urls` | array | Category or product URLs |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `fetchDetails` | boolean | Include full product information |
| `fetchReviews` | boolean | Include customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `proxy` | object | Connection settings |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/walgreens-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `articleId` | string |
| `hairToolType` | string |
| `size` | list |
| `toothPasteAttribute` | string |
| `storeInv` | string |
| `fulfillerType` | string |
| `webExclusive` | string |
| `wic` | string |
| `skuInvAvailMap` | object |
| `prodId` | string |
| `skuId` | string |
| `imageUrl` | string |
| `upc` | string |
| `productURL` | string |
| `reviewCount` | string |
| `productSize` | string |
| `newItem` | string |
| `wBrandInd` | string |
| `autoReorder` | string |
| `unitPrice` | string |
| `unitPriceSize` | string |
| `loyaltyEligible` | string |
| `reviewURL` | string |
| `ingredientName` | string |
| `inactiveIngredients` | string |
| `pln` | string |
| `imageUrl220` | string |
| `imageUrl450` | string |
| `productName` | string |
| `imageUrl50` | string |
| `productType` | string |
| `isAgeRestricted` | boolean |
| `excludeLocalDelivery` | boolean |
| `sameDayPurchaseLimit` | integer |
| `storeUPC` | string |
| `temperatureCode` | list |
| `gtin` | string |
| `shipToStoreInd` | string |
| `oddEnabled` | boolean |
| `tier1CategoryId` | string |

---

[← All scrapers](../../README.md)
