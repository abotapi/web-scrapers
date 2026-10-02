# Pap.fr Scraper

Extract property listings from pap.fr. Get fully-detailed listings with price, address, rooms, area, photo gallery, description, and arrondissement/department/region geography.

**[Open Pap.fr Scraper on Apify](https://apify.com/abotapi/pap-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pap-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "filter", "locations": [{"city": "Paris"}], "listingType": "Buy", "propertyType": "Apartment", "sortBy": "Default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "IT"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `locations` | array | Locations to search (Filter mode) |
| `listingType` | string | Buy or rent (Filter mode) |
| `propertyType` | string | Property type (Filter mode) |
| `roomsMin` | integer | Min rooms / pièces (Filter mode) |
| `sortBy` | string | Sort order (Filter mode) |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total listings |
| `fetchDetails` | boolean | Visit each listing's detail page |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pap-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `listingType` | string |
| `propertyType` | string |
| `title` | string |
| `priceValue` | integer |
| `priceCurrency` | string |
| `priceDisplay` | string |
| `rooms` | integer |
| `livingSpace` | float |
| `bedrooms` | integer |
| `floor` | integer |
| `hoaChargesYearly` | null |
| `propertyTaxYearly` | null |
| `heatingType` | string |
| `description` | string |
| `streetAddress` | string |
| `city` | string |
| `postcode` | string |
| `arrondissement` | string |
| `department` | string |
| `region` | string |
| `latitude` | null |
| `longitude` | null |
| `energyClass` | string |
| `ghgClass` | string |
| `isActive` | boolean |
| `reference` | string |
| `sellerPhone` | string |
| `seller` | object |
| `refusesCommercialSolicitation` | boolean |
| `imageCount` | integer |
| `images` | list |
| `additionalProperties` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
