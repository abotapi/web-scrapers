# Trade Me NZ Scraper

Scrape trademe.co.nz across all five sections: Marketplace goods and auctions, Property, Motors, Jobs and Services. Search or paste URLs, walk pagination, and enrich with full detail plus seller feedback (positive/negative counts and score).

**[Open Trade Me NZ Scraper on Apify](https://apify.com/abotapi/trademe-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~trademe-co-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"vertical": "marketplace", "mode": "search", "queries": ["iphone"], "listingType": "residential-sale", "sort": "Default", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `vertical` | string | Section |
| `mode` * | string | Mode |
| `queries` | array | Keyword searches |
| `listingType` | string | Property listing type |
| `region` | string | Region |
| `district` | string | District |
| `suburb` | string | Suburb |
| `propertyType` | string | Property type |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `minLandArea` | integer | Min land area (m²) |
| `maxLandArea` | integer | Max land area (m²) |
| `minFloorArea` | integer | Min floor area (m²) |
| `maxFloorArea` | integer | Max floor area (m²) |
| `petsOkay` | boolean | Pets okay |
| `make` | string | Vehicle make |
| `model` | string | Vehicle model |
| `minYear` | integer | Min year |
| `maxYear` | integer | Max year |
| `minOdometer` | integer | Min odometer (km) |
| `maxOdometer` | integer | Max odometer (km) |
| `bodyStyle` | string | Body style |
| `transmission` | string | Transmission |
| `fuel` | string | Fuel type |
| `category` | string | Category |
| `condition` | string | Condition |
| `buyNowOnly` | boolean | Buy Now only |
| `jobType` | string | Job type |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `startUrls` | array | URLs |
| `sort` | string | Sort order |
| `keyword` | string | Extra keyword filter |
| `fetchDetails` | boolean | Fetch full details  seller feedback |
| `includeMemberFeedbackComments` | boolean | Include individual feedback comments |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/trademe-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `vertical` | string |
| `title` | string |
| `url` | string |
| `category` | string |
| `priceDisplay` | string |
| `startPrice` | integer |
| `buyNowPrice` | float |
| `hasBuyNow` | boolean |
| `region` | string |
| `suburb` | string |
| `district` | null |
| `photoUrls` | list |
| `listedDate` | string |
| `closesDate` | string |
| `isFeatured` | null |
| `sponsored` | null |
| `sellerType` | string |
| `memberId` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
