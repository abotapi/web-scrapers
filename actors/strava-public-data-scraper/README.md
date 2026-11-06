# Strava Data Scraper

Scrape public Strava data: clubs (members, location, sport, settings), athlete profiles and every current challenge (goals, dates, participants, qualifying activities). Club directory discovery, monitoring (NEW, UPDATED, EXPIRED), incremental runs, resume, MCP export.

**[Open Strava Data Scraper on Apify](https://apify.com/abotapi/strava-public-data-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~strava-public-data-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "challenges", "challengeSports": ["promoted", "run", "ride", "swim", "walk", "hike", "workout"], "links": ["https://www.strava.com/clubs/23629", "https://www.strava.com/clubs/ambleside-ac", "23629", "ambleside-ac", "https://www.strava.com/athletes/2619603"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `challengeSports` | array | Challenge sports (Challenges mode) |
| `fetchChallengeDetails` | boolean | Read challenge detail pages |
| `links` | array | Links (Clubs / Athletes mode) |
| `discoverCount` | integer | Clubs to discover (Discover mode) |
| `discoverOffset` | integer | Directory start offset |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/strava-public-data-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `kind` | string |
| `challengeId` | string |
| `name` | string |
| `shortName` | string |
| `url` | string |
| `slug` | string |
| `sport` | string |
| `goal` | integer |
| `dimension` | string |
| `sponsored` | boolean |
| `icon` | string |
| `coverImageUrl` | string |
| `coverTitleText` | null |
| `logoUrl` | string |
| `logoTitleText` | null |
| `followersInChallenge` | null |
| `joined` | boolean |
| `externalJoinUrl` | null |
| `goalDescription` | string |
| `rewardDescription` | string |
| `dateStart` | string |
| `dateEnd` | string |
| `raw` | object |
| `subtitle` | string |
| `activityType` | string |
| `ended` | boolean |
| `completed` | boolean |
| `rewardButtonText` | string |
| `locale` | string |
| `organizingClub` | object |
| `overviewText` | string |
| `rewardsText` | string |
| `rulesText` | string |
| `additionalInfoText` | string |
| `qualifyingActivities` | list |
| `participantsCount` | integer |
| `goalDescriptionDetail` | string |

---

[← All scrapers](../../README.md)
