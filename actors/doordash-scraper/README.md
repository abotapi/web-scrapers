# DoorDash Scraper

Extract structured doordash.com data at scale. Search by keyword or paste store URLs to get store details, ratings, price tier, location, full menus, contact info, opening hours, review insights, star-rating breakdowns, and Google rating data.

**[Open DoorDash Scraper on Apify](https://apify.com/abotapi/doordash-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~doordash-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "search": ["pizza"], "storeType": "any", "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `search` | array | Search queries |
| `location` | string | Location (optional) |
| `storeType` | string | Store type |
| `ratedOnly` | boolean | Well-rated only |
| `dealsOnly` | boolean | Deals only |
| `urls` | array | Store URLs or IDs |
| `includeMenu` | boolean | Include menu |
| `includeBusiness` | boolean | Include contact & hours |
| `includeReviews` | boolean | Include reviews |
| `maxStores` | integer | Max stores |
| `maxPages` | integer | Max search pages |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/doordash-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `storeId` | string |
| `name` | string |
| `url` | string |
| `description` | string |
| `storeBio` | null |
| `isConvenience` | boolean |
| `isShippingOnly` | boolean |
| `rating` | float |
| `ratingCount` | integer |
| `ratingCountDisplay` | string |
| `priceTier` | string |
| `cuisines` | list |
| `currency` | string |
| `isDashpass` | boolean |
| `offersDelivery` | boolean |
| `offersPickup` | boolean |
| `offersCatering` | boolean |
| `offersGroupOrder` | boolean |
| `offersScheduling` | boolean |
| `additionalImages` | list |
| `etaMinutes` | integer |
| `pickupEtaMinutes` | integer |
| `deliveryFee` | string |
| `coverImageUrl` | string |
| `coverSquareImageUrl` | string |
| `businessHeaderImageUrl` | string |
| `photoCountText` | null |
| `businessId` | string |
| `businessName` | string |
| `businessLink` | string |
| `businessTags` | list |
| `distance` | string |
| `latitude` | float |
| `longitude` | float |
| `city` | string |
| `state` | string |
| `street` | string |
| `displayAddress` | string |
| `isSponsored` | boolean |
| `distanceMiles` | float |

---

[← All scrapers](../../README.md)
