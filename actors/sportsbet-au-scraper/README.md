# Sportsbet AU Scraper

Scrape sportsbet.com.au odds: events, markets, selections and prices for AFL, NRL, soccer, cricket, tennis and more, plus horse, greyhound and harness racing with runners, jockeys, trainers, form and tote prices. Search by sport or race type, or paste page URLs.

**[Open Sportsbet AU Scraper on Apify](https://apify.com/abotapi/sportsbet-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~sportsbet-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "sports", "sports": ["Australian Rules"], "competitions": ["AFL"], "eventKind": "all", "raceTypes": ["horse"], "raceDate": "today", "raceRegion": "all", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `category` | string | What to search |
| `sports` | array | Sports |
| `competitions` | array | Competitions |
| `eventKind` | string | Event kind |
| `raceTypes` | array | Race types |
| `raceDate` | string | Race date |
| `raceRegion` | string | Race region |
| `trackNames` | array | Tracks |
| `upcomingOnly` | boolean | Upcoming races only |
| `marketNames` | array | Market names |
| `minOdds` | number | Minimum win price |
| `maxOdds` | number | Maximum win price |
| `eachwayOnly` | boolean | Each-way markets only |
| `urls` | array | Page URLs |
| `fetchDetails` | boolean | Fetch full market detail |
| `maxPages` | integer | Max pages per run |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Change scope |
| `compactUpdates` | boolean | Compact updates |
| `expireAfterMissedScans` | integer | Expire after missed scans |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/sportsbet-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `rowId` | string |
| `eventId` | integer |
| `externalId` | string |
| `name` | string |
| `displayName` | string |
| `sport` | string |
| `classId` | integer |
| `competitionId` | integer |
| `competitionName` | string |
| `region` | string |
| `startTime` | string |
| `startTimeEpoch` | integer |
| `eventSort` | string |
| `numMarkets` | integer |
| `status` | string |
| `hasBIR` | boolean |
| `isLive` | boolean |
| `isFuture` | boolean |
| `liveStream` | boolean |
| `sameGameMultiEnabled` | boolean |
| `url` | string |
| `marketId` | integer |
| `marketName` | string |
| `marketType` | string |
| `marketSort` | string |
| `marketStatus` | string |
| `eachwayAvailable` | boolean |
| `cashoutAvailable` | boolean |
| `selectionId` | integer |
| `selectionName` | string |
| `resultType` | string |
| `selectionStatus` | string |
| `winPrice` | float |
| `winPriceNum` | integer |
| `winPriceDen` | integer |
| `priceCode` | string |
| `multiplesKey` | string |
| `impliedProbability` | float |
| `priceRank` | integer |

---

[← All scrapers](../../README.md)
