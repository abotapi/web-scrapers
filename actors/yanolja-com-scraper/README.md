# Yanolja Scraper

Scrape Yanolja (NOL), Korea's largest accommodations marketplace, by region or URL. Every row carries name, address, coordinates, phone, star class, room types with per-night rates, review score and review text, amenities, policies and photos from one stay page read.

**[Open Yanolja Scraper on Apify](https://apify.com/abotapi/yanolja-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yanolja-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["서울"], "categoryGroup": "all", "sortResultsBy": "site_order", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "KR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Regions and places |
| `categoryGroup` | string | Stay group |
| `urls` | array | Yanolja URLs |
| `minPriceKrw` | integer | Minimum price (KRW) |
| `maxPriceKrw` | integer | Maximum price (KRW) |
| `sortResultsBy` | string | Order the returned rows by |
| `fetchDetails` | boolean | Fetch full stay details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max collection pages per region |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yanolja-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `stayId` | string |
| `rowType` | string |
| `url` | string |
| `name` | string |
| `listingImageUrl` | string |
| `collectionSlug` | string |
| `collectionTitle` | string |
| `subtitle` | null |
| `stayGroup` | string |
| `hotelStar` | null |
| `badges` | list |
| `locationDescription` | string |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `cityName` | string |
| `cityDetail` | string |
| `sellerPhone` | string |
| `ratingValue` | float |
| `reviewCount` | integer |
| `replyCount` | integer |
| `ratingFromFd` | float |
| `ratingCountFromFd` | integer |
| `priceRange` | string |
| `lowestPriceKrw` | integer |
| `overnightPriceKrw` | integer |
| `dayUsePriceKrw` | integer |
| `overnightSoldOut` | boolean |
| `dayUseSoldOut` | boolean |
| `checkInDate` | string |
| `checkOutDate` | string |
| `checkInTime` | null |
| `checkOutTime` | null |
| `description` | null |
| `descriptionText` | null |
| `facilities` | list |
| `mainImageUrl` | string |
| `photoUrls` | list |
| `roomPhotoUrls` | list |

---

[← All scrapers](../../README.md)
