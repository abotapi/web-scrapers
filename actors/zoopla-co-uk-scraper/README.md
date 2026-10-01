# Zoopla Scraper

Scrape UK property from Zoopla: for sale, to rent and Land Registry sold prices. Search by place with filters or paste links. Optional full detail adds EPC, floor plans, tenure, price history, stations and agent phone. Incremental mode for change monitoring.

**[Open Zoopla Scraper on Apify](https://apify.com/abotapi/zoopla-co-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zoopla-co-uk-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["London"], "channels": ["for-sale"], "radius": "0", "sortBy": "recommended", "soldPeriodMonths": "all-time", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Places to search |
| `channels` | array | Channels |
| `minPrice` | integer | Minimum price (GBP) |
| `maxPrice` | integer | Maximum price (GBP) |
| `minBeds` | integer | Minimum bedrooms |
| `maxBeds` | integer | Maximum bedrooms |
| `minBaths` | integer | Minimum bathrooms |
| `propertySubTypes` | array | Property types |
| `radius` | string | Search radius (miles) |
| `addedSince` | string | Added to site |
| `keywords` | string | Keyword |
| `sortBy` | string | Sort results by |
| `chainFreeOnly` | boolean | Chain free only |
| `auctionOnly` | boolean | Auction properties only |
| `sharedOwnershipOnly` | boolean | Shared ownership only |
| `retirementOnly` | boolean | Retirement homes only |
| `reducedPriceOnly` | boolean | Reduced price only |
| `includeUnderOffer` | boolean | Include under offer / sold STC |
| `includeLetAgreed` | boolean | Include let agreed |
| `furnishedState` | string | Furnishing |
| `priceFrequency` | string | Rent price shown per |
| `petsAllowed` | boolean | Pets allowed only |
| `billsIncluded` | boolean | Bills included only |
| `soldPeriodMonths` | string | Sold within |
| `startUrls` | array | Zoopla links |
| `includeDetails` | boolean | Fetch full listing details |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per place and channel |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zoopla-co-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `listingType` | string |
| `channel` | string |
| `url` | string |
| `title` | string |
| `address` | string |
| `summaryDescription` | string |
| `price` | integer |
| `priceLabel` | string |
| `priceQualifier` | string |
| `currency` | string |
| `rentFrequencyLabel` | null |
| `priceDrop` | object |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `receptionRooms` | integer |
| `propertyType` | string |
| `sizeSqft` | integer |
| `sizeSource` | string |
| `publishedOn` | string |
| `publishedOnLabel` | string |
| `availableFrom` | null |
| `statusFlag` | null |
| `underOffer` | null |
| `isPremium` | boolean |
| `featuredType` | string |
| `displayType` | string |
| `tags` | list |
| `highlights` | list |
| `buyerIncentives` | list |
| `latitude` | null |
| `longitude` | null |
| `imageUrl` | string |
| `imageCaption` | string |
| `images` | list |
| `imageCount` | integer |
| `floorPlanCount` | integer |
| `videoCount` | integer |
| `branchName` | string |
| `branchId` | integer |

---

[← All scrapers](../../README.md)
