# Resy Scraper

Scrape Resy restaurants and live reservation availability by city or URL. Get bookable times by date and party size, plus ratings, cuisine, price, phone, website, photos, and coordinates. Includes availability monitoring, resume, and MCP export.

**[Open Resy Scraper on Apify](https://apify.com/abotapi/resy-restaurant-availability-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~resy-restaurant-availability-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "cities": ["new-york-ny"], "orderBy": "availability", "date": "today", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `query` | string | Keyword or cuisine |
| `radiusMiles` | integer | Search radius (miles) |
| `orderBy` | string | Sort results by |
| `resyCreditEligibleOnly` | boolean | Card-credit eligible restaurants only |
| `venueUrls` | array | Restaurant links |
| `urls` | array | Restaurant links (alias) |
| `date` | string | Date |
| `partySize` | integer | Party size |
| `timeFilter` | string | Earliest time (optional) |
| `maxItems` | integer | Max items |
| `fetchDetails` | boolean | Read the full profile for each restaur |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/resy-restaurant-availability-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `venueId` | integer |
| `url` | string |
| `name` | string |
| `urlSlug` | string |
| `citySlug` | string |
| `cityName` | string |
| `neighborhood` | string |
| `locality` | string |
| `region` | string |
| `country` | string |
| `streetAddress` | null |
| `postalCode` | null |
| `crossStreet` | null |
| `latitude` | float |
| `longitude` | float |
| `cuisine` | list |
| `priceRange` | integer |
| `priceRangeSymbol` | string |
| `rating` | float |
| `ratingCount` | integer |
| `phone` | string |
| `website` | null |
| `menuUrl` | null |
| `images` | list |
| `imageUrl` | string |
| `whyWeLikeIt` | string |
| `about` | null |
| `collections` | list |
| `maxPartySize` | integer |
| `minPartySize` | null |
| `currencyCode` | string |
| `currencySymbol` | string |
| `isGlobalDiningAccess` | boolean |
| `isResyCreditEligible` | null |
| `isTockInventory` | boolean |
| `resySelect` | null |
| `googlePlaceId` | null |
| `venueGroupName` | null |

---

[← All scrapers](../../README.md)
