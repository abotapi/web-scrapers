# Willhaben.at Scraper

Scrape Willhaben.at listings into clean JSON with 40+ structured fields, including prices, GPS coordinates, photos, dates, seller details and category-specific attributes. Search with filters or paste any Willhaben URL.

**[Open Willhaben.at Scraper on Apify](https://apify.com/abotapi/willhaben-at-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~willhaben-at-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "kaufen-und-verkaufen/marktplatz", "sort": "default", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AT"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `category` | string | Category |
| `categoryPath` | string | Custom category path (advanced) |
| `keyword` | string | Keyword |
| `areaId` | integer | Area ID (location) |
| `minPrice` | integer | Min price () |
| `maxPrice` | integer | Max price () |
| `sort` | string | Sort by |
| `customParameters` | array | Extra filters (advanced) |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch detail pages |
| `maxListings` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/willhaben-at-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `uuid` | string |
| `url` | string |
| `seoUrl` | string |
| `verticalId` | integer |
| `adTypeId` | integer |
| `productId` | integer |
| `advertStatus` | string |
| `category` | string |
| `title` | string |
| `description` | string |
| `price` | integer |
| `priceDisplay` | string |
| `country` | string |
| `state` | string |
| `district` | string |
| `postcode` | string |
| `locationName` | string |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `publishedDate` | string |
| `changedDate` | string |
| `endDate` | string |
| `isPrivate` | boolean |
| `orgId` | string |
| `advertiserLabel` | null |
| `images` | list |
| `imageCount` | integer |
| `mainImage` | string |
| `teaserAttributes` | list |
| `advertiserInfo` | object |
| `rawAttributes` | list |
| `attr_LOCATION` | string |
| `attr_p2penabled` | string |
| `attr_CHANGED` | string |
| `attr_categorytreeattributeids` | string |
| `attr_CHANGED_String` | string |
| `attr_POSTCODE` | string |
| `attr_BODY_DYN` | string |

---

[← All scrapers](../../README.md)
