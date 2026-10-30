# Drom.ru Scraper

Scrape drom.ru vehicle listings: make/model/year/mileage, price, engine and transmission specs, public masked VIN, seller type and the full specifications table. Make+region search with filters or paste links. Resume, incremental updates and MCP export included.

**[Open Drom.ru Scraper on Apify](https://apify.com/abotapi/drom-auto-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~drom-auto-listings-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "makes": ["audi"], "statisticsSort": "newest", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "RU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `makes` | array | Makes (search and statistics mode) |
| `minYear` | integer | Min year |
| `maxYear` | integer | Max year |
| `region` | string | Region slug (search mode) |
| `minPrice` | integer | Min price (RUB, search mode) |
| `maxPrice` | integer | Max price (RUB, search mode) |
| `transmission` | integer | Transmission (search mode) |
| `drivetrain` | integer | Drivetrain (search mode) |
| `models` | array | Models (statistics mode) |
| `minPriceYen` | integer | Min sale price (JPY, statistics mode) |
| `maxPriceYen` | integer | Max sale price (JPY, statistics mode) |
| `statisticsSort` | string | Sort (statistics mode) |
| `listingUrls` | array | Links (urls mode) |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/drom-auto-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `make` | string |
| `model` | string |
| `year` | string |
| `price` | integer |
| `currency` | string |
| `engine` | string |
| `fuel` | string |
| `gearbox` | string |
| `drivetrain` | string |
| `mileageKm` | integer |
| `city` | string |
| `bullId` | integer |
| `minimalPrice` | integer |
| `description` | string |
| `images` | object |
| `frameType` | integer |
| `showPlaceholder` | boolean |
| `dealType` | integer |
| `sold` | boolean |
| `marks` | list |
| `info` | null |
| `dealerName` | null |
| `hasDealerName` | boolean |
| `subtitle` | string |
| `attributes` | list |
| `promotionStatus` | integer |
| `date` | string |
| `location` | string |
| `carState` | list |
| `region` | string |
| `category` | string |
| `engineVolume` | integer |
| `powerHp` | integer |
| `photos` | list |
| `photoCount` | integer |
| `imageUrl` | string |
| `recordType` | string |

---

[← All scrapers](../../README.md)
