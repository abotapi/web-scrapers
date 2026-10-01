# Subito.it Scraper

Scrape Subito.it listings across cars, real estate, marketplace, jobs, and more. Search by keyword and filters or use Subito URLs. Returns prices, descriptions, photos, specs, seller details, location, 60+ fields, and optional seller reputation.

**[Open Subito.it Scraper on Apify](https://apify.com/abotapi/subito-it-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~subito-it-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"category": "marketplace", "sellerType": "any", "sort": "datedesc", "adType": "s", "startUrls": [{"url": "https://www.subito.it/annunci-italia/vendita/usato/?q=bici"}], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "IT"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `category` * | string | Vertical |
| `searchQuery` | string | Search query |
| `subjectOnly` | boolean | Search title only |
| `region` | string | Region |
| `city` | string | Province / city |
| `town` | string | Town (comune) |
| `priceMin` | integer | Min price (EUR) |
| `priceMax` | integer | Max price (EUR) |
| `sellerType` | string | Advertiser type |
| `sort` | string | Sort order |
| `adType` | string | Ad type |
| `condition` | array | Item condition |
| `shippableOnly` | boolean | Shippable only |
| `brand` | string | Brand id |
| `model` | string | Model id |
| `yearMin` | integer | Min registration year |
| `yearMax` | integer | Max registration year |
| `mileageMin` | integer | Min mileage (km) |
| `mileageMax` | integer | Max mileage (km) |
| `fuelType` | array | Fuel type |
| `gearbox` | string | Gearbox |
| `bodyType` | array | Body type |
| `vehicleStatus` | array | Vehicle condition |
| `sizeMin` | integer | Min surface (m²) |
| `sizeMax` | integer | Max surface (m²) |
| `roomsMin` | integer | Min rooms |
| `roomsMax` | integer | Max rooms |
| `bathroomsMin` | integer | Min bathrooms |
| `buildingCondition` | array | Building condition |
| `jobCategory` | array | Job sector |
| `contractType` | array | Contract type |
| `workHours` | string | Working hours |
| `educationDegree` | string | Education level |
| `startUrls` | array | Start URLs |
| `scrapeDetail` | boolean | Fetch full vehicle details |
| `scrapeReviews` | boolean | Fetch seller reputation |
| `maxItems` | integer | Max items (total) |
| `maxItemsPerQuery` | integer | Max items per search |
| `proxyConfiguration` * | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/subito-it-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `urn` | string |
| `url` | string |
| `mobileUrl` | string |
| `title` | string |
| `description` | string |
| `price` | integer |
| `priceRaw` | string |
| `currency` | string |
| `adType` | string |
| `adTypeKey` | string |
| `category` | string |
| `categoryId` | string |
| `categorySlug` | string |
| `macrocategoryId` | string |
| `reference` | null |
| `postedAt` | string |
| `postedAtRaw` | string |
| `expiresAt` | string |
| `scrapedAt` | string |
| `region` | string |
| `regionId` | string |
| `city` | string |
| `cityId` | string |
| `cityShort` | string |
| `town` | string |
| `townId` | string |
| `imageCount` | integer |
| `images` | list |
| `images360` | list |
| `sellerId` | string |
| `sellerName` | null |
| `sellerType` | string |
| `isCompany` | boolean |
| `sellerPhone` | null |
| `sellerVat` | null |
| `shopId` | null |
| `shopName` | null |
| `shippingAvailable` | boolean |
| `shippingType` | null |

---

[← All scrapers](../../README.md)
