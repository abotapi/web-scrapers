# FotMob Scraper

Pull structured football data from FotMob: match details with scores, team stats, events, lineups, player ratings, H2H, league tables and fixtures, team squads, and player careers. Paste match URLs, pull fixtures by date, or scrape leagues, teams and players.

**[Open FotMob Scraper on Apify](https://apify.com/abotapi/fotmob-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fotmob-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "news", "date": "2026-08-29", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `matchIds` | array | Match ids or links |
| `urls` | array | FotMob links (any mix) |
| `date` | string | Fixtures date |
| `daysAhead` | integer | Extra days after the date |
| `leagueIds` | array | Leagues |
| `season` | string | Season (optional, league mode only) |
| `teamIds` | array | Teams |
| `playerIds` | array | Players |
| `newsPages` | integer | News listing pages to read |
| `includePlayerStats` | boolean | Player stats |
| `includeEvents` | boolean | Match events & shotmap |
| `includeLineups` | boolean | Match lineups |
| `includeTeamStats` | boolean | Team stats |
| `includeH2H` | boolean | Head-to-head & league table |
| `includeRawData` | boolean | Raw page data |
| `includeNewsBody` | boolean | News article full body |
| `maxItems` | integer | Max records |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fotmob-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | string |
| `name` | string |
| `title` | string |
| `lead` | string |
| `source` | string |
| `sourceIconUrl` | string |
| `imageUrl` | string |
| `publishedAt` | string |
| `language` | string |
| `url` | string |
| `matchUrl` | string |
| `scrapedAt` | string |
| `bodyHtml` | string |
| `bodyText` | string |

---

[← All scrapers](../../README.md)
