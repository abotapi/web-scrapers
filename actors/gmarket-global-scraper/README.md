# Gmarket.co.kr Scraper

Scrape Gmarket.co.kr product listings and customer reviews into clean JSON. Search by keyword, paste product URLs, or use review-only mode with a product ID. Fast, simple, and built for structured ecommerce data collection.

**[Open Gmarket.co.kr Scraper on Apify](https://apify.com/abotapi/gmarket-global-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gmarket-global-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["laptop"], "maxReviewsPerProduct": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `keywords` | array | Keywords |
| `minPrice` | integer | Minimum price (KRW) |
| `maxPrice` | integer | Maximum price (KRW) |
| `overseaDeliveryOnly` | boolean | Oversea delivery only |
| `bigSmileOnly` | boolean | BigSmile promotion only |
| `urls` | array | URLs |
| `reviewsOnly` | boolean | Reviews only |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total records |
| `fetchDetails` | boolean | Fetch detail pages (richer default) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gmarket-global-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `goodsCode` | string |
| `title` | string |
| `linkUrl` | string |
| `imageUrl` | string |
| `additionalImages` | list |
| `sellPriceKrw` | integer |
| `originalPriceKrw` | string |
| `salePriceKrw` | string |
| `currencyPrice` | string |
| `discountRate` | string |
| `wasPriceKrw` | null |
| `currentPriceKrw` | integer |
| `savingsAmountKrw` | null |
| `discountRatePercent` | null |
| `isOnSpecial` | boolean |
| `isBigSmilePromo` | boolean |
| `bigSmileImageUrl` | null |
| `isSponsored` | boolean |
| `isFreeShipping` | boolean |
| `deliveryInfo` | string |
| `deliveryFee` | string |
| `sellerCustNo` | string |
| `miniShopHandle` | string |
| `miniShopUrl` | string |
| `categoryCodeL` | string |
| `categoryCodeM` | string |
| `categoryCodeS` | string |
| `overseaDeliveryAvailable` | boolean |
| `isBigSmile` | boolean |
| `isAdult` | boolean |
| `translation` | object |
| `raw` | object |
| `scrapedAt` | string |
| `descriptionText` | null |
| `brand` | string |
| `sellerInfo` | object |
| `sellerCompanyName` | string |
| `sellerManagerName` | string |
| `sellerPhone` | string |
| `sellerBusinessNumber` | string |

---

[← All scrapers](../../README.md)
