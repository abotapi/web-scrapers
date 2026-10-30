# Sportsbook Odds Scraper (1xBet, Melbet, Linebet, Paripulse)

Collect live and prematch betting odds from 1xBet, Melbet, Linebet and Paripulse. Give it the brands and feeds you want and get one row per event with its 1X2 prices, over/under lines, teams, league and start time.

**[Open Sportsbook Odds Scraper (1xBet, Melbet, Linebet, Paripulse) on Apify](https://apify.com/abotapi/sportsbook-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~sportsbook-odds-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "bulk", "bookmakers": ["linebet"], "feeds": ["prematch"], "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Collection mode |
| `bookmakers` | array | Bookmakers |
| `feeds` | array | Feeds |
| `eventUrls` | array | Match URLs |
| `sports` | array | Sports (optional filter) |
| `eventsPerRequest` | integer | Events per request |
| `maxEvents` | integer | Max events |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/sportsbook-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `bookmaker` | string |
| `feed` | string |
| `eventId` | string |
| `num` | integer |
| `sport` | string |
| `sportId` | integer |
| `league` | string |
| `leagueId` | integer |
| `home` | string |
| `away` | string |
| `startTime` | string |
| `startTs` | integer |
| `period` | null |
| `scoreHome` | null |
| `scoreAway` | null |
| `isLive` | boolean |
| `oddsHome` | float |
| `oddsDraw` | float |
| `oddsAway` | float |
| `totals` | list |
| `markets` | list |
| `url` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
