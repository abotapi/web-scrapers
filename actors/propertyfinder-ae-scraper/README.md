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
  -d '{"mode": "search", "locations": ["dubai"], "category": "buy", "propertyTypes": ["properties"], "sort": "nd", "listedWithin": "any", "virtualViewing": "any", "rentPeriod": "yearly", "furnishing": "any", "completionStatus": "any", "directorySort": "featured", "transactionsPeriod": "1m", "transactionsSort": "newest", "maxReviewsPerArea": 10, "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | What do you want to scrape |
| `locations` | array | Locations |
| `category` | string | Category |
| `propertyTypes` | array | Property types |
| `sort` | string | Sort listings by |
| `keywords` | string | Keywords |
| `listedWithin` | string | Listed within |
| `virtualViewing` | string | Virtual viewing |
| `propertyCondition` | array | Property condition |
| `mortgageCashbackOnly` | boolean | Mortgage cashback only (for sale) |
| `rentPeriod` | string | Rent period (for rent) |
| `minCheques` | integer | Min number of cheques (for rent) |
| `maxCheques` | integer | Max number of cheques (for rent) |
| `urls` | array | Search page URLs |
| `minPrice` | integer | Min price (AED) |
| `maxPrice` | integer | Max price (AED) |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `maxBathrooms` | integer | Max bathrooms |
| `minAreaSqft` | integer | Min size (sqft) |
| `maxAreaSqft` | integer | Max size (sqft) |
| `minPricePerSqft` | integer | Min price per sqft (AED) |
| `maxPricePerSqft` | integer | Max price per sqft (AED) |
| `furnishing` | string | Furnishing |
| `completionStatus` | string | Completion status |
| `amenities` | array | Amenities |
| `dealBadges` | array | Deal badges |
| `verifiedOnly` | boolean | Verified listings only |
| `superAgentOnly` | boolean | SuperAgent listings only |
| `searchText` | string | Name search |
| `directorySort` | string | Sort by |
| `agentLanguages` | array | Languages spoken (agents only) |
| `agentNationality` | string | Nationality (agents only) |
| `transactionsPeriod` | string | Period |
| `transactionsFrom` | string | From date |
| `transactionsTo` | string | To date |
| `transactionsSort` | string | Sort transactions by |
| `maxReviewsPerArea` | integer | Max reviews per area |
| `maxListings` | integer | Max results |
| `maxPages` | integer | Max pages per search |
| `includeDetails` | boolean | Add listing details (listing modes, ex |
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
