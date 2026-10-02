# Auction.com Scraper

Extract foreclosure, REO, short-sale, and auction listings from Auction.com in minutes. Search by location and property filters or paste any Auction.com URL. Get 45+ structured fields, including auction dates, bids, estimated values, occupancy status, coordinates, and photos.

**[Open Auction.com Scraper on Apify](https://apify.com/abotapi/auction-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~auction-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "states": ["CA"], "listingStatus": "active", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `states` | array | States |
| `city` | string | City |
| `zipCodes` | array | ZIP codes |
| `keyword` | string | Keyword / address |
| `listingStatus` | string | Listing status |
| `propertyTypes` | array | Property types |
| `assetTypes` | array | Asset types |
| `auctionFormats` | array | Auction formats |
| `minBeds` | integer | Min bedrooms |
| `maxBeds` | integer | Max bedrooms |
| `minBaths` | integer | Min bathrooms |
| `minSqft` | integer | Min square footage |
| `maxSqft` | integer | Max square footage |
| `minPrice` | integer | Min starting bid |
| `maxPrice` | integer | Max starting bid |
| `sortBy` | string | Sort by |
| `urls` | array | Auction.com URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/auction-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `urn` | string |
| `url` | string |
| `listingStatus` | string |
| `listingStatusGroup` | string |
| `listingStatusLabel` | string |
| `isHot` | null |
| `address` | string |
| `addressLine1` | string |
| `city` | string |
| `state` | string |
| `zip` | string |
| `county` | string |
| `latitude` | float |
| `longitude` | float |
| `propertyTypeCode` | string |
| `propertyTypeGroup` | string |
| `assetType` | string |
| `productType` | string |
| `occupancyStatus` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `squareFootage` | null |
| `lotSize` | null |
| `yearBuilt` | null |
| `propertyValuation` | null |
| `startingBid` | null |
| `auctionType` | string |
| `auctionStartDate` | string |
| `auctionEndDate` | null |
| `auctionVisibleStartDate` | string |
| `isOnline` | boolean |
| `nosAmount` | null |
| `estimatedValue` | null |
| `estimatedValueLow` | null |
| `estimatedValueHigh` | null |
| `estimatedValueType` | null |
| `rentalEstimate` | null |
| `rentalEstimateLow` | null |
| `rentalEstimateHigh` | null |

---

[← All scrapers](../../README.md)
