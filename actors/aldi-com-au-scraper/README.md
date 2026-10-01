# ALDI AU Scraper

Scrape ALDI Australia (aldi.com.au) products: name, brand, price, was-price, savings, unit price, size, category, images, availability and Special Buys on-sale date, plus full detail (ingredients, allergens, nutrition). Search by keyword or category, filter by brand/theme, or paste any ALDI URL.

**[Open ALDI AU Scraper on Apify](https://apify.com/abotapi/aldi-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~aldi-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["milk"], "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `categories` | array | Categories |
| `specialsCategory` | string | Specials / offers range |
| `excludeCategories` | array | Exclude departments |
| `brands` | array | Brands |
| `themes` | array | Themes |
| `sortBy` | string | Sort by |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per term/category |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/aldi-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `sku` | string |
| `abstractSku` | string |
| `name` | string |
| `title` | string |
| `brand` | string |
| `slug` | string |
| `url` | string |
| `price` | float |
| `priceDisplay` | string |
| `wasPrice` | null |
| `wasPriceDisplay` | null |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `savingsDisplay` | null |
| `promoLabel` | null |
| `onSale` | boolean |
| `unitPrice` | float |
| `unitPriceDisplay` | string |
| `unitOfMeasure` | string |
| `unitMeasure` | string |
| `perUnitPrice` | null |
| `perUnitPriceDisplay` | null |
| `perUnitQuantity` | null |
| `perUnitQuantityUnit` | null |
| `priceAdditionalInfo` | null |
| `bottleDeposit` | integer |
| `bottleDepositDisplay` | string |
| `feeText` | null |
| `currency` | string |
| `currencySymbol` | string |
| `sellingSize` | string |
| `quantityUnit` | string |
| `weightType` | string |
| `purchaseQuantity` | object |
| `onSaleDate` | null |
| `onSaleDateDisplay` | null |
| `isSpecialBuy` | boolean |
| `notForSale` | boolean |
| `notForSaleReason` | null |

---

[← All scrapers](../../README.md)
