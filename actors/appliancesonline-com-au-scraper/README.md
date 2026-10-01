# Appliances Online Scraper

Scrape appliancesonline.com.au by category, keyword, or URL. Extract title, brand, AUD price, was-price, stock, key specs, images, ratings, badges, care plans, manuals, delivery details, questions, and customer reviews.

**[Open Appliances Online Scraper on Apify](https://apify.com/abotapi/appliancesonline-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~appliancesonline-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "categories", "searchInputs": ["washers-and-dryers/washing-machines"], "productInputs": ["176381", "appliancesonline.com.au/product/8kg-front-load-haier-washing-machine-hwm80-1403d/", "appliancesonline.com.au/filter/washers-and-dryers/washing-machines/", "appliancesonline.com.au/filter/clearance/"], "sortBy": "popularity", "maxReviewsPerProduct": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchInputs` | array | Categories or keywords |
| `productInputs` | array | Product links, category/sale links or  |
| `facets` | array | Facet slugs (advanced, optional) |
| `brand` | string | Brand |
| `onSaleOnly` | boolean | Only reduced products |
| `inStockOnly` | boolean | Only in-stock products |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `sortBy` | string | Sort results |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `fetchQuestions` | boolean | Fetch questions |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `questionsCap` | integer | Max questions per product |
| `maxItems` | integer | Max products |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/appliancesonline-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `title` | string |
| `url` | string |
| `brand` | null |
| `manufacturer` | object |
| `price` | integer |
| `rrp` | integer |
| `savings` | integer |
| `onSale` | boolean |
| `altPriceMsg` | null |
| `inStock` | null |
| `stockStatus` | null |
| `stockByWarehouse` | null |
| `available` | boolean |
| `featured` | boolean |
| `featuredLabel` | null |
| `ribbonType` | null |
| `popularity` | null |
| `badges` | list |
| `isGreenProduct` | boolean |
| `carePlans` | list |
| `associatedFreeProducts` | null |
| `efficiencyLabels` | null |
| `image` | string |
| `images` | list |
| `media` | list |
| `dimensions` | null |
| `specs` | object |
| `keySpecs` | null |
| `attr` | null |
| `warrantyNote` | null |
| `modelNumber` | null |
| `manufacturerNumber` | null |
| `origin` | null |
| `energyCalculatorEnabled` | boolean |
| `features` | list |
| `manuals` | list |
| `delivery` | null |
| `questions` | null |

---

[← All scrapers](../../README.md)
