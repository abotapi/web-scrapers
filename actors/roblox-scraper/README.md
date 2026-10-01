# Roblox Scraper

Scrape Roblox experiences, marketplace items, users and communities. Player counts, visits, likes, genre, creator, resale prices and price history, limited status, follower counts, community members and roles. Search, ids or pasted links, with incremental change tracking for scheduled runs.

**[Open Roblox Scraper on Apify](https://apify.com/abotapi/roblox-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~roblox-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "games", "gameQueries": ["blox fruits"], "catalogCategory": "all", "userQueries": ["builderman"], "groupQueries": ["7"], "catalogSalesType": "any", "catalogSortType": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `gameQueries` | array | Experience searches or ids |
| `catalogKeyword` | string | Catalog keyword |
| `catalogCategory` | string | Catalog category |
| `userQueries` | array | Usernames, ids or profile links |
| `userKeyword` | string | Username search |
| `groupQueries` | array | Community ids or links |
| `fetchGroupMembers` | boolean | Also return community members |
| `urls` | array | Roblox links |
| `minPlaying` | integer | Minimum live players |
| `catalogSalesType` | string | Sale type |
| `catalogSortType` | string | Sort order |
| `minPrice` | integer | Minimum price (Robux) |
| `maxPrice` | integer | Maximum price (Robux) |
| `fetchDetails` | boolean | Fetch full details |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items (total, default 20, 0  unlim |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/roblox-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `id` | integer |
| `universeId` | integer |
| `rootPlaceId` | integer |
| `url` | string |
| `name` | string |
| `description` | string |
| `creatorId` | integer |
| `creatorName` | string |
| `creatorType` | string |
| `creatorHasVerifiedBadge` | boolean |
| `genre` | string |
| `genreL1` | string |
| `genreL2` | string |
| `price` | null |
| `playing` | integer |
| `visits` | integer |
| `maxPlayers` | integer |
| `favoritedCount` | integer |
| `upVotes` | integer |
| `downVotes` | integer |
| `likeRatio` | float |
| `createdAt` | string |
| `updatedAt` | string |
| `copyingAllowed` | boolean |
| `createVipServersAllowed` | boolean |
| `universeAvatarType` | string |
| `isContentRestricted` | boolean |
| `iconUrl` | string |
| `sampledServerCount` | integer |
| `sampledServerPlayers` | integer |
| `avgServerFps` | float |
| `avgServerPing` | float |
| `mediaImageCount` | integer |
| `mediaVideoCount` | integer |
| `badges` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
