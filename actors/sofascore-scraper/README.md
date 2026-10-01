# SofaScore Scraper

Pull structured sports data from SofaScore across football, basketball, tennis, and 20+ sports. Search by keyword, paste URLs, fetch live matches, or download fixtures by date. Returns scores, stats, lineups, incidents, odds, teams, players, tournaments, and more.

**[Open SofaScore Scraper on Apify](https://apify.com/abotapi/sofascore-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~sofascore-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["Real Madrid"], "searchType": "all", "sports": ["football"], "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search queries |
| `searchType` | string | Restrict search to type |
| `urls` | array | SofaScore URLs |
| `sports` | array | Sports |
| `date` | string | Date (Scheduled mode) |
| `daysAhead` | integer | Extra days |
| `includeStatistics` | boolean | Match statistics |
| `includeLineups` | boolean | Match lineups |
| `includeIncidents` | boolean | Match incidents |
| `includeOdds` | boolean | Match odds |
| `includeVotes` | boolean | Fan votes (reviews) |
| `includeH2H` | boolean | Head-to-head history |
| `includeStandings` | boolean | Tournament standings |
| `includeSquad` | boolean | Team squad |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/sofascore-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | integer |
| `sport` | string |
| `name` | string |
| `fullName` | string |
| `shortName` | string |
| `nameCode` | string |
| `gender` | string |
| `national` | boolean |
| `ranking` | null |
| `country` | string |
| `tournament` | string |
| `tournamentId` | integer |
| `managerName` | string |
| `venue` | string |
| `venueCity` | string |
| `venueCapacity` | integer |
| `teamColors` | object |
| `foundationDate` | integer |
| `logo` | string |
| `url` | string |
| `raw` | object |
| `pregameForm` | object |

---

[← All scrapers](../../README.md)
