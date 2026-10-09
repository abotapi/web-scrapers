# Kijiji.ca Scraper

Scrape Kijiji.ca listings across property, vehicles, jobs, electronics, furniture, services, and more. Search by keyword and location or use any Kijiji URL. Extract titles, descriptions, prices, photos, GPS coordinates, seller details, and category-specific attributes.

**[Open Kijiji.ca Scraper on Apify](https://apify.com/abotapi/kijiji-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kijiji-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["iphone"], "location": "city-of-toronto", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "CA"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | array | Keywords |
| `location` | string | Location |
| `sortBy` | string | Sort by |
| `urls` | array | Kijiji URLs |
| `minPrice` | integer | Min price (CAD) |
| `maxPrice` | integer | Max price (CAD) |
| `fetchDetails` | boolean | Fetch listing details |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kijiji-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listingType` | string |
| `title` | string |
| `description` | string |
| `url` | string |
| `categoryId` | integer |
| `adSource` | string |
| `activationDate` | string |
| `sortingDate` | string |
| `imageCount` | integer |
| `imageUrls` | list |
| `price` | null |
| `priceRaw` | null |
| `priceType` | string |
| `originalPrice` | null |
| `currency` | string |
| `locationId` | integer |
| `locationName` | string |
| `address` | string |
| `nearestIntersection` | null |
| `latitude` | float |
| `longitude` | float |
| `posterId` | string |
| `posterRating` | null |
| `posterVerified` | boolean |
| `sellerType` | string |
| `posterInfo` | object |
| `isTopAd` | boolean |
| `isPriceDrop` | boolean |
| `hasVirtualTour` | null |
| `flags` | object |
| `attr_phonecarrier` | string |
| `attr_payment` | string |
| `attr_phonebrand` | string |
| `attr_fulfillment` | list |
| `attr_forsaleby` | string |
| `attr_srpLogoUrl` | string |
| `attributesRaw` | list |
| `views` | integer |
| `status` | string |

---

[← All scrapers](../../README.md)
