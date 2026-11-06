# Cian RU Scraper

Collect property listings from Cian.ru by search filters or direct URLs. Returns structured rows with listing URL, title, price, address, rooms, area, floors, photos, visible contact fields, coordinates when available, and optional detail-page enrichment.

**[Open Cian RU Scraper on Apify](https://apify.com/abotapi/cian-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~cian-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "location": "Москва", "operationType": "sale", "sort": "default", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `urls` | array | URLs |
| `location` | string | Location |
| `regionId` | integer | Region ID |
| `operationType` | string | Operation |
| `category` | string | Category |
| `sort` | string | Sort |
| `rooms` | array | Rooms |
| `includeStudio` | boolean | Include studio |
| `minPrice` | integer | Min price (RUB) |
| `maxPrice` | integer | Max price (RUB) |
| `minArea` | integer | Min area |
| `maxArea` | integer | Max area |
| `minFloor` | integer | Min floor |
| `maxFloor` | integer | Max floor |
| `minFloors` | integer | Min building floors |
| `maxFloors` | integer | Max building floors |
| `minLivingArea` | integer | Min living area |
| `maxLivingArea` | integer | Max living area |
| `minHouseYear` | integer | Min house build year |
| `maxHouseYear` | integer | Max house build year |
| `minCeilingHeight` | number | Min ceiling height (m) |
| `maxCeilingHeight` | number | Max ceiling height (m) |
| `isByHomeowner` | boolean | Only from owners |
| `fromDeveloper` | boolean | Only from developers |
| `isFirstFloor` | boolean | Only first floor |
| `notLastFloor` | boolean | Not last floor |
| `hasVideo` | boolean | With video |
| `withLayout` | boolean | With floor plan |
| `shortTermRent` | boolean | Short-term (daily) rent |
| `repair` | array | Renovation types |
| `publishPeriod` | string | Published within |
| `advancedFilters` | object | Advanced Cian filters |
| `maxItems` * | integer | Max items |
| `maxPages` | integer | Max pages |
| `fetchDetails` | boolean | Fetch listing details |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/cian-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `url` | string |
| `sourceUrl` | string |
| `title` | string |
| `jkName` | string |
| `price` | string |
| `priceValue` | integer |
| `pricePerMeter` | integer |
| `currency` | string |
| `address` | string |
| `district` | string |
| `metro` | string |
| `metroTime` | integer |
| `metroLineId` | integer |
| `metroLineColor` | string |
| `roomsCount` | integer |
| `totalArea` | float |
| `livingArea` | float |
| `kitchenArea` | float |
| `floorNumber` | integer |
| `floorsCount` | integer |
| `buildYear` | null |
| `materialType` | string |
| `dealType` | string |
| `category` | string |
| `offerType` | string |
| `isFromDeveloper` | boolean |
| `isPremium` | boolean |
| `isApartments` | boolean |
| `phoneNumbers` | list |
| `latitude` | float |
| `longitude` | float |
| `description` | string |
| `formattedFullInfo` | string |
| `imageUrls` | list |
| `mainImage` | object |
| `siteUrl` | string |
| `formattedAddress` | string |
| `formattedFullPrice` | string |
| `ceilingHeight` | integer |

---

[← All scrapers](../../README.md)
