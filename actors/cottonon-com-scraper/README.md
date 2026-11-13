# Cotton On Scraper

Scrape the Cotton On Group storefronts: Cotton On, Body, Kids, Typo, Factorie and Supre. Category, sale and gift listings with prices and colors, full product details, sizes and member reviews. Search and URL modes with sorting and scheduled change tracking.

**[Open Cotton On Scraper on Apify](https://apify.com/abotapi/cottonon-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~cottonon-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "urls", "urls": ["https://cottonon.com/AU/co/women/womens-clothing/womens-tops/", "https://cottonon.com/AU/kids/kids-boys-1-8/boys-1-8-clothing/", "https://cottonon.com/AU/typo/typo-shop-all/", "https://cottonon.com/AU/factorie/f-shop-all/", "https://cottonon.com/AU/co/co-sale/", "https://cottonon.com/AU/co/co-gifts/", "https://cottonon.com/AU/hold-me-cami/2060406-02.html"], "searchTerms": ["denim shorts"], "market": "AU", "sort": "relevance", "maxReviews": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `urls` | array | Catalog links (any mix) |
| `searchTerms` | array | Keywords |
| `market` | string | Market |
| `sort` | string | Sort |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch member reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/cottonon-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `familyId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `brandId` | string |
| `color` | string |
| `price` | float |
| `wasPrice` | float |
| `discountPercent` | null |
| `currency` | string |
| `categories` | list |
| `categoryPath` | list |
| `description` | string |
| `imageUrl` | string |
| `imageAltUrl` | string |
| `imageUrls` | list |
| `ean` | string |
| `eans` | list |
| `rmsDivision` | string |
| `rmsDepartment` | string |
| `rmsCategory` | string |
| `sourceKind` | string |
| `sourceLabel` | string |
| `position` | integer |
| `listName` | string |
| `colorCount` | integer |
| `colorName` | string |
| `colors` | list |
| `sizes` | list |
| `sizesUnavailable` | list |
| `fitFeedback` | string |
| `sizeNote` | string |
| `availability` | string |
| `reviewsAverage` | float |
| `reviewsCount` | integer |
| `reviewsRecommended` | null |
| `ratingDistribution` | list |
| `reviews` | list |

---

[← All scrapers](../../README.md)
