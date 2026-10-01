# Property Finder UAE Scraper

Scrape PropertyFinder.ae listings at scale. Extract prices, property details, images, amenities, coordinates, agent contacts, broker info, RERA numbers and more for UAE real estate research and analysis.

**[Open Property Finder UAE Scraper on Apify](https://apify.com/abotapi/propertyfinder-ae-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~propertyfinder-ae-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "scrapeType": "listings", "category": "buy", "locations": ["dubai"], "propertyTypes": ["properties"], "sort": "nd", "listedWithin": "any", "virtualViewing": "any", "rentPeriod": "yearly", "directorySort": "featured", "transactionsPeriod": "1m", "transactionsSort": "newest", "maxReviewsPerArea": 10, "furnishing": "any", "completionStatus": "any", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. How will you supply the input |
| `scrapeType` | string | 2. What do you want to scrape |
| `category` | string | Category (listings, agents, brokers, t |
| `locations` | array | Locations (all types) |
| `propertyTypes` | array | Property types (listings, transactions |
| `sort` | string | Sort listings by |
| `keywords` | string | Keywords (listings) |
| `listedWithin` | string | Listed within (listings) |
| `virtualViewing` | string | Virtual viewing (listings) |
| `propertyCondition` | array | Property condition (listings) |
| `mortgageCashbackOnly` | boolean | Mortgage cashback only (listings for s |
| `rentPeriod` | string | Rent period (listings for rent) |
| `minCheques` | integer | Min number of cheques (listings for re |
| `maxCheques` | integer | Max number of cheques (listings for re |
| `searchText` | string | Name search (agents, brokers) |
| `directorySort` | string | Sort agents & brokers by |
| `agentLanguages` | array | Languages spoken (agents) |
| `agentNationality` | string | Nationality (agents) |
| `transactionsPeriod` | string | Period (transactions) |
| `transactionsFrom` | string | From date (transactions) |
| `transactionsTo` | string | To date (transactions) |
| `transactionsSort` | string | Sort transactions by |
| `maxReviewsPerArea` | integer | Max reviews per area (area insights) |
| `urls` | array | Search page URLs (URL mode, listings) |
| `minPrice` | integer | Min price, AED (listings, transactions |
| `maxPrice` | integer | Max price, AED (listings, transactions |
| `minBedrooms` | integer | Min bedrooms (listings, transactions) |
| `maxBedrooms` | integer | Max bedrooms (listings, transactions) |
| `minBathrooms` | integer | Min bathrooms (listings) |
| `maxBathrooms` | integer | Max bathrooms (listings) |
| `minAreaSqft` | integer | Min size, sqft (listings, transactions |
| `maxAreaSqft` | integer | Max size, sqft (listings, transactions |
| `minPricePerSqft` | integer | Min price per sqft, AED (listings) |
| `maxPricePerSqft` | integer | Max price per sqft, AED (listings) |
| `furnishing` | string | Furnishing (listings) |
| `completionStatus` | string | Completion status (listings) |
| `amenities` | array | Amenities (listings) |
| `dealBadges` | array | Deal badges (listings) |
| `verifiedOnly` | boolean | Verified listings only |
| `superAgentOnly` | boolean | SuperAgent listings only |
| `maxListings` | integer | Max results (all types) |
| `maxPages` | integer | Max pages per search (listings, agents |
| `includeDetails` | boolean | Add listing details (listings, extra c |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/propertyfinder-ae-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `title` | string |
| `description` | string |
| `price` | integer |
| `currency` | string |
| `price_period` | string |
| `price_hidden` | boolean |
| `price_per_sqft` | integer |
| `payment_method` | list |
| `number_of_cheques` | null |
| `mortgage_cashback` | integer |
| `property_type` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `size_sqft` | integer |
| `size_unit` | string |
| `furnished` | string |
| `completion_status` | string |
| `offering_type` | string |
| `location` | string |
| `city` | string |
| `community` | string |
| `subcommunity` | string |
| `building` | string |
| `latitude` | float |
| `longitude` | float |
| `agent_name` | string |
| `agent_email` | string |
| `agent_phone` | string |
| `agent_whatsapp` | string |
| `agent_is_super` | boolean |
| `agent_image` | string |
| `agent_languages` | list |
| `broker_name` | string |
| `broker_phone` | string |
| `broker_email` | string |
| `broker_logo` | string |
| `rera_number` | null |
| `reference` | string |
| `listed_date` | string |

---

[← All scrapers](../../README.md)
