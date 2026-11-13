# Naver Land Scraper

Scrape structured property listings from Naver Land map URLs. Extract listing titles, prices, areas, addresses, GPS coordinates, property types, transaction types and source links for clean real estate datasets.

**[Open Naver Land Scraper on Apify](https://apify.com/abotapi/naver-land-listings?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~naver-land-listings/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchKeywords": ["잠실"], "startUrls": ["https://new.land.naver.com/complexes?ms=2AM2Zq,3zhF96,16&a=APT:ABYG:JGC&e=RETAIL", "https://new.land.naver.com/complexes/111380", "https://new.land.naver.com/article/2651481309", "https://new.land.naver.com/complexes?sk=%EC%9E%A0%EC%8B%A4"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "KR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchKeywords` | array | Search keywords |
| `startUrls` | array | Naver Land URLs |
| `locations` | array | Locations (region names) |
| `dealType` | string | Deal type |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Minimum price (KRW) |
| `maxPrice` | integer | Maximum price (KRW) |
| `minArea` | integer | Minimum area (m2) |
| `maxArea` | integer | Maximum area (m2) |
| `onlyOwners` | boolean | Owner-verified only |
| `maxItems` | integer | Maximum listings |
| `fetchDetails` | boolean | Fetch listing details |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/naver-land-listings?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | null |
| `url` | string |
| `detailUrl` | string |
| `buildingName` | null |
| `complexNumber` | string |
| `unit` | null |
| `dealType` | null |
| `dealTypeKo` | null |
| `propertyTypeCode` | string |
| `propertyTypeKo` | string |
| `rentPrice` | null |
| `managementFee` | null |
| `priceChangeStatus` | null |
| `areaExclusive` | null |
| `areaSupply` | null |
| `areaSupplyLabel` | null |
| `totalFloors` | integer |
| `buildYear` | string |
| `city` | string |
| `district` | string |
| `neighbourhood` | string |
| `regionCode` | string |
| `isOwnerVerified` | null |
| `confirmedDate` | null |
| `brokerageName` | null |
| `brokerName` | null |
| `sameAddressCount` | null |
| `photoCount` | null |
| `featureText` | null |
| `isDirectTrade` | null |
| `roomCount` | null |
| `bathRoomCount` | null |
| `parkingCount` | null |
| `parkingPerHousehold` | null |
| `movingInType` | null |
| `movingInNegotiable` | null |
| `priceLabel` | null |
| `id` | string |
| `articleNo` | null |
| `complexNo` | string |

---

[← All scrapers](../../README.md)
