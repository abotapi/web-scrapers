# Zigbang Scraper

Scrape Zigbang property listings across Seoul and South Korea, including one-room, villa and officetel rentals and sales. Extract deposits, monthly rent, prices, floor plans, property details, subway access, locations and agent contacts.

**[Open Zigbang Scraper on Apify](https://apify.com/abotapi/zigbang-property-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zigbang-property-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "강남역", "serviceType": "oneroom", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `urls` | array | Listing URLs or ids |
| `query` | string | Location keyword |
| `serviceType` | string | Listing type |
| `subwayRadiusKm` | integer | Subway radius (km) |
| `geohash` | string | Geohash cell (advanced) |
| `salesTypes` | array | Deal types |
| `depositMin` | integer | Min deposit (만원) |
| `depositMax` | integer | Max deposit (만원) |
| `rentMin` | integer | Min monthly rent (만원) |
| `rentMax` | integer | Max monthly rent (만원) |
| `manageCostMin` | integer | Min maintenance fee (만원) |
| `manageCostMax` | integer | Max maintenance fee (만원) |
| `sizeMin` | number | Min size (m2) |
| `sizeMax` | number | Max size (m2) |
| `fetchDetails` | boolean | Fetch listing details |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zigbang-property-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | integer |
| `url` | string |
| `serviceType` | string |
| `title` | string |
| `salesType` | string |
| `deposit` | integer |
| `rent` | integer |
| `manageCost` | string |
| `sizeM2` | float |
| `supplyAreaM2` | float |
| `exclusiveAreaM2` | float |
| `roomType` | string |
| `roomTypeTitle` | null |
| `floor` | string |
| `buildingFloor` | string |
| `registeredAt` | string |
| `isNew` | boolean |
| `status` | boolean |
| `tags` | list |
| `badges` | list |
| `address` | string |
| `city` | string |
| `district` | string |
| `neighborhood` | string |
| `lat` | float |
| `lng` | float |
| `thumbnailUrl` | string |

---

[← All scrapers](../../README.md)
