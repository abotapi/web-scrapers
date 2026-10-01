# Drogasil Brazil Pharmacy Scraper

Scrape Drogasil (drogasil.com.br) medicines, health and beauty products by keyword, catalogue section or pasted link. Returns EAN, brand, price in BRL, discount, multi-buy price, stock, images, variants and the regulatory block. Incremental mode tracks daily changes.

**[Open Drogasil Brazil Pharmacy Scraper on Apify](https://apify.com/abotapi/drogasil-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~drogasil-com-br-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["dipirona"], "soldBy": "any", "prescriptionFilter": "any", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categories` | array | Catalogue sections |
| `urls` | array | Store links |
| `brands` | array | Brand |
| `minPrice` | integer | Minimum price (BRL) |
| `maxPrice` | integer | Maximum price (BRL) |
| `soldBy` | string | Sold by |
| `excludeKits` | boolean | Exclude multi-product kits |
| `prescriptionFilter` | string | Prescription requirement |
| `inStockOnly` | boolean | Only products currently in stock |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword, section  |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/drogasil-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `image` | string |
| `images` | list |
| `currency` | string |
| `price` | float |
| `packSize` | string |
| `prescriptionRequired` | boolean |
| `isGenericMedicine` | boolean |
| `isKit` | boolean |
| `requiresRefrigeration` | boolean |
| `soldBy` | string |
| `categories` | list |
| `categoryPath` | string |
| `productGroup` | string |
| `pharmaceuticalForm` | null |
| `drugClassificationCode` | integer |
| `badges` | list |
| `variantCount` | integer |
| `variantAttributes` | list |
| `isSponsored` | boolean |
| `ean` | string |
| `originalPrice` | float |
| `discountPercent` | float |
| `onSale` | boolean |
| `multiBuyUnitPrice` | null |
| `multiBuyMinQuantity` | null |
| `pixPrice` | null |
| `pixDiscountPercent` | null |
| `installments` | list |
| `stockQuantity` | integer |
| `inStock` | boolean |
| `breadcrumb` | list |
| `description` | string |
| `shortDescription` | string |
| `longDescription` | null |
| `usageInstructions` | string |

---

[← All scrapers](../../README.md)
