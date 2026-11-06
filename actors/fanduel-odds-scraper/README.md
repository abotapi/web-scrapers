# FanDuel Odds Scraper

Scrape FanDuel sportsbook odds, including moneylines, spreads, totals, player props and futures. Extract decimal, fractional and American odds, live event markers and kickoff times. Supports scheduled incremental monitoring to track odds changes.

**[Open FanDuel Odds Scraper on Apify](https://apify.com/abotapi/fanduel-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fanduel-odds-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "popular", "sports": ["American Football", "Basketball"], "region": "NJ", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `sports` | array | Sports (sports mode) |
| `urls` | array | Links (links mode) |
| `region` | string | Sportsbook region |
| `liveOnly` | boolean | Live games only |
| `fetchSgpMarkets` | boolean | Same Game Parlay markets per event |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fanduel-odds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `eventId` | string |
| `matchup` | string |
| `home` | string |
| `away` | string |
| `homeAbbr` | string |
| `awayAbbr` | string |
| `homeLogo` | string |
| `awayLogo` | string |
| `kickoffTime` | string |
| `inplay` | boolean |
| `competitionId` | integer |
| `competition` | string |
| `sport` | string |
| `moneyline` | object |
| `spread` | null |
| `total` | null |
| `oddsTimestamp` | string |
| `url` | string |
| `detailFetched` | boolean |

---

[← All scrapers](../../README.md)
