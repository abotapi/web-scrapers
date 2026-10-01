# Crexi Scraper

Scrape crexi.com commercial listings: asking price, cap rate, square footage, units, year built, lot size, APN, zoning, address, coordinates, status, photos plus agent and brokerage contacts and 100+ fields. Search by city, ZIP or keyword with type, price and sort filters, or paste URLs.

**[Open Crexi Scraper on Apify](https://apify.com/abotapi/crexi-commercial-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~crexi-commercial-listings-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Austin, TX"], "sortBy": "rank", "sortDirection": "Descending", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations or keywords |
| `propertyTypes` | array | Property types |
| `priceMin` | integer | Minimum asking price (USD) |
| `priceMax` | integer | Maximum asking price (USD) |
| `includeUnpriced` | boolean | Include unpriced listings |
| `sortBy` | string | Sort by |
| `sortDirection` | string | Sort direction |
| `urls` | array | Crexi.com URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/crexi-commercial-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `globalId` | string |
| `property_id` | integer |
| `name` | string |
| `title` | string |
| `urlSlug` | string |
| `url` | string |
| `property_url` | string |
| `detailPageUrl` | string |
| `askingPrice` | integer |
| `price` | integer |
| `types` | list |
| `property_type` | string |
| `status` | string |
| `description` | string |
| `thumbnailUrl` | string |
| `imageUrl` | string |
| `image_url` | string |
| `brokerLogoUrl` | null |
| `brokerTeamLogoUrl` | string |
| `numberOfImages` | integer |
| `numberOfGalleryItems` | integer |
| `brokerageName` | string |
| `brokerage` | string |
| `isInOpportunityZone` | boolean |
| `isNew` | boolean |
| `hasVideo` | boolean |
| `hasOM` | boolean |
| `hasFlyer` | boolean |
| `hasVirtualTour` | boolean |
| `showCountdownAsDate` | boolean |
| `userIsAssetOwner` | boolean |
| `activatedOn` | string |
| `updatedOn` | string |
| `fullAddress` | string |
| `propertyAddress` | string |
| `address` | string |
| `city` | string |
| `county` | string |
| `state` | string |

---

[← All scrapers](../../README.md)
