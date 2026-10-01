# Homes.com Scraper

Scrape US property records from Homes.com. Pick a city, state or ZIP and a channel (for sale, for rent, recently sold, open houses, foreclosures), or paste links. One flat row per property with price, beds, baths, size, address, geo, agent and brokerage.

**[Open Homes.com Scraper on Apify](https://apify.com/abotapi/homes-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~homes-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "location": "Austin, TX", "sort": "relevance", "listingType": "for_sale", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `location` | string | Location |
| `zipCode` | string | ZIP code (optional) |
| `minBedrooms` | integer | Bedrooms |
| `maxPrice` | integer | Maximum price (USD) |
| `sort` | string | Sort order |
| `urls` | array | Homes.com links |
| `listingType` | string | Listing channel |
| `fetchDetails` | boolean | Fetch full property details |
| `maxItems` | integer | Max items (per run, 0  unlimited) |
| `maxPages` | integer | Max pages per search (0  unlimited) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/homes-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingKey` | string |
| `url` | string |
| `listingChannel` | string |
| `isSold` | boolean |
| `name` | string |
| `description` | string |
| `price` | integer |
| `priceCurrency` | string |
| `availability` | string |
| `propertyType` | string |
| `bedrooms` | integer |
| `bathrooms` | float |
| `livingAreaSqft` | integer |
| `yearBuilt` | null |
| `streetAddress` | string |
| `city` | string |
| `state` | string |
| `postalCode` | string |
| `country` | string |
| `latitude` | null |
| `longitude` | null |
| `primaryImageUrl` | string |
| `datePosted` | null |
| `dateModified` | null |
| `brokerageName` | string |
| `agentName` | string |
| `agentTitle` | string |
| `agentUrl` | null |
| `agentPhone` | string |
| `agentEmail` | null |
| `scrapedAt` | string |
| `statusLabel` | string |

---

[← All scrapers](../../README.md)
