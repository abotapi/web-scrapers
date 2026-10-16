# The RealReal Scraper

Scrape luxury consignment listings from therealreal.com. Browse by designer, category or keyword and get designer, item class, condition grade, retail price versus current list price, measurements, materials and authentication notes. Built for price positioning per brand per category.

**[Open The RealReal Scraper on Apify](https://apify.com/abotapi/therealreal-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~therealreal-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "categories": ["women/handbags"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `categories` | array | Category paths |
| `designers` | array | Designers |
| `designerCategory` | string | Category for the designers above |
| `urls` | array | The RealReal links |
| `designer` | string | Designer |
| `condition` | string | Condition grade |
| `color` | string | Colour |
| `minPrice` | integer | Minimum list price (USD) |
| `maxPrice` | integer | Maximum list price (USD) |
| `availableOnly` | boolean | Only items still available |
| `onSaleOnly` | boolean | Only marked-down items |
| `vintageOnly` | boolean | Only vintage items |
| `editorsPickOnly` | boolean | Only editors' picks |
| `withTagsOnly` | boolean | Only items with original tags |
| `fetchDetails` | boolean | Read each item's page |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max result pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/therealreal-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `sku` | string |
| `variantId` | string |
| `name` | string |
| `url` | string |
| `designer` | string |
| `designerId` | string |
| `artist` | null |
| `itemClass` | list |
| `category` | string |
| `condition` | string |
| `conditionNote` | null |
| `color` | string |
| `gender` | string |
| `primaryMaterial` | string |
| `attributes` | object |
| `retailPrice` | null |
| `listPrice` | integer |
| `originalPrice` | integer |
| `currency` | string |
| `discountPct` | integer |
| `vsRetailPct` | null |
| `isOnSale` | boolean |
| `availability` | string |
| `isSold` | boolean |
| `quantity` | string |
| `obsessionCount` | integer |
| `isEditorsPick` | null |
| `badge` | null |
| `images` | list |
| `imageCount` | integer |
| `sourceUrl` | string |
| `detailFetched` | boolean |
| `measurements` | null |
| `materials` | null |
| `description` | null |
| `authenticationNote` | null |
| `sustainability` | null |
| `returnPolicy` | null |
| `disclaimers` | null |

---

[← All scrapers](../../README.md)
