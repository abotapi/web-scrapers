# ResQ Club Scraper

Scrape ResQ Club surplus food offers in Finland, Sweden and Estonia: name, price, current price, discount, portions left, pickup and order windows, tags and photo, plus the venue address, phone, website, coordinates and ratings. Search by area, name or country, or paste venue links.

**[Open ResQ Club Scraper on Apify](https://apify.com/abotapi/resq-club-surplus-food-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~resq-club-surplus-food-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["60.1699,24.9384"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Areas to search |
| `radiusKm` | integer | Radius (km) |
| `searchPhrase` | string | Venue name contains |
| `includeVenuesWithoutOffers` | boolean | Also return venues with no offer right |
| `urls` | array | Venue links or ids |
| `countries` | array | Countries |
| `tags` | array | Offer tags |
| `includeSoldOutOffers` | boolean | Include sold-out offers |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max venue pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/resq-club-surplus-food-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `offerId` | integer |
| `url` | string |
| `offerName` | string |
| `offerDescription` | string |
| `price` | float |
| `currentPrice` | float |
| `priceMinorUnits` | integer |
| `currentPriceMinorUnits` | integer |
| `currency` | string |
| `discountPercent` | integer |
| `unitsLeft` | integer |
| `isSoldOut` | boolean |
| `pickupStart` | string |
| `pickupEnd` | string |
| `orderStart` | string |
| `orderEnd` | string |
| `tags` | list |
| `tagNames` | list |
| `imageUrl` | null |
| `venueId` | integer |
| `venueUrl` | string |
| `venueName` | string |
| `venueDescription` | null |
| `address` | string |
| `country` | string |
| `countryName` | string |
| `latitude` | float |
| `longitude` | float |
| `phone` | string |
| `website` | string |
| `isBestOf` | boolean |
| `isNewVenue` | boolean |
| `venueOffersLeft` | integer |
| `venueUnitsLeft` | integer |
| `venueLanguage` | string |
| `distanceKm` | float |
| `reviewsGood` | integer |
| `reviewsOkay` | integer |
| `reviewsBad` | integer |

---

[← All scrapers](../../README.md)
