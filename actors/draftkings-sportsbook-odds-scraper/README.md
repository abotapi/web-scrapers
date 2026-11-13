# DraftKings Scraper

Scrape DraftKings Sportsbook odds, game lines, team totals, player and game props, futures, Pick6 multipliers and final scores. Extract DFS contests, entry fees, prize pools, player salaries and stats. Includes nested markets with American, decimal and fractional odds.

**[Open DraftKings Scraper on Apify](https://apify.com/abotapi/draftkings-sportsbook-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~draftkings-sportsbook-odds-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "sportSlugs": ["basketball"], "marketGroups": ["game-lines"], "state": "auto", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `sportSlugs` | array | Sports |
| `leagues` | array | Leagues (optional) |
| `marketGroups` | array | Market groups |
| `includeDfs` | boolean | Include DFS contests & players |
| `dfsSport` | string | DFS sport (optional) |
| `state` | string | Book state |
| `urls` | array | Sportsbook links |
| `fetchDetails` | boolean | Detail enrichment |
| `includeResults` | boolean | Final scores of past games |
| `resultsDaysBack` | integer | Results days back |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/draftkings-sportsbook-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | null |
| `matchKey` | string |
| `resultsEventId` | string |
| `source` | string |
| `name` | string |
| `sport` | string |
| `league` | string |
| `sportName` | string |
| `leagueName` | string |
| `leagueId` | string |
| `startTime` | string |
| `status` | string |
| `statusDetail` | string |
| `homeTeam` | string |
| `awayTeam` | string |
| `homeTeamAbbr` | string |
| `awayTeamAbbr` | string |
| `homeScore` | integer |
| `awayScore` | integer |
| `winner` | string |
| `winnerTeam` | string |
| `venue` | string |
| `seasonName` | string |
| `capturedAt` | string |
| `changeType` | string |
| `changedFields` | list |
| `firstSeenAt` | string |
| `lastSeenAt` | string |

---

[← All scrapers](../../README.md)
