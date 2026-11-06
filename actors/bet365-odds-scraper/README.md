# bet365 Odds Scraper

Scrape bet365 live in-play and pre-match odds across 20+ sports. Extract fixture listings, full event betting markets, decimal odds and price snapshots. Supports scheduled incremental monitoring to track odds changes over time.

**[Open bet365 Odds Scraper on Apify](https://apify.com/abotapi/bet365-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bet365-odds-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "live", "sport": "soccer", "region": "GB", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `sport` | string | Sport (sport mode) |
| `urls` | array | Event links (urls mode) |
| `region` | string | Site region |
| `fetchDetails` | boolean | Read full market boards (urls mode) |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bet365-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `home` | string |
| `away` | string |
| `matchup` | string |
| `status` | string |
| `prices` | list |
| `hasLiveMedia` | boolean |
| `sport` | string |
| `resultOdds` | null |
| `fixtureId` | string |
| `sportId` | string |
| `competition` | string |
| `competitionId` | string |
| `leagueCode` | string |
| `round` | null |
| `homeTeamId` | string |
| `awayTeamId` | string |
| `inPlay` | boolean |
| `startTime` | string |
| `url` | string |
| `oddsTimestamp` | string |

---

[← All scrapers](../../README.md)
