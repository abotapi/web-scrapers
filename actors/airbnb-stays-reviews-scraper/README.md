# Airbnb Scraper

Scrape Airbnb stays by destination or link: nightly and total price, rating breakdown, host stats, amenities, house rules, coordinates, photos, and the full review history with text and star ratings. Dual mode, filters, incremental monitoring, resume, MCP export.

**[Open Airbnb Scraper on Apify](https://apify.com/abotapi/airbnb-stays-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~airbnb-stays-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["Paris, France"], "currency": "USD", "maxItems": 10, "maxReviewsPerListing": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Destinations |
| `listingUrls` | array | Listing and search links |
| `urls` | array | Listing and search links (alias) |
| `checkIn` | string | Check-in |
| `checkOut` | string | Check-out |
| `adults` | integer | Adults |
| `children` | integer | Children |
| `infants` | integer | Infants |
| `pets` | integer | Pets |
| `currency` | string | Currency |
| `priceMin` | integer | Minimum price per night |
| `priceMax` | integer | Maximum price per night |
| `roomTypes` | array | Stay types |
| `minBedrooms` | integer | Minimum bedrooms |
| `minBeds` | integer | Minimum beds |
| `minBathrooms` | integer | Minimum bathrooms |
| `superhostOnly` | boolean | Superhost stays only |
| `instantBookOnly` | boolean | Instant Book stays only |
| `guestFavoriteOnly` | boolean | Guest favourites only |
| `maxItems` | integer | Max items |
| `fetchDetails` | boolean | Read full detail for every listing |
| `includeReviews` | boolean | Read the review history |
| `maxReviewsPerListing` | integer | Max reviews per listing |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/airbnb-stays-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `categoryLabel` | string |
| `stayCategory` | string |
| `locationLabel` | string |
| `subtitle` | string |
| `badges` | null |
| `isGuestFavorite` | null |
| `latitude` | float |
| `longitude` | float |
| `checkIn` | string |
| `checkOut` | string |
| `adults` | integer |
| `images` | list |
| `imagesCount` | integer |
| `detailLoaded` | boolean |
| `reviewsFetched` | integer |
| `rating` | null |
| `reviewsCount` | null |
| `priceLabel` | string |
| `priceTotal` | integer |
| `priceOriginalTotal` | null |
| `pricePerNight` | float |
| `pricePerNightListed` | integer |
| `priceCurrency` | string |
| `priceCurrencyRequested` | string |
| `priceQualifier` | string |
| `nights` | integer |
| `bedrooms` | null |
| `beds` | null |
| `bathrooms` | null |
| `cardHighlights` | list |

---

[← All scrapers](../../README.md)
