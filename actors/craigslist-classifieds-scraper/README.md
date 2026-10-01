# Craigslist Scraper

Scrape Craigslist postings in any of 700+ cities worldwide: price, title, posting text, attributes, photos, coordinates, neighbourhood and posted date. Search by city, section, keyword and price, or paste search and posting links. Incremental monitoring, resume, MCP export.

**[Open Craigslist Scraper on Apify](https://apify.com/abotapi/craigslist-classifieds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~craigslist-classifieds-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "cities": ["sfbay"], "category": "sss", "query": "bicycle", "soldBy": "all", "sortBy": "rel", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `category` | string | Section |
| `query` | string | Keyword |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `soldBy` | string | Posted by |
| `hasImage` | boolean | Only postings with photos |
| `postedToday` | boolean | Only postings from today |
| `sortBy` | string | Sort by |
| `startUrls` | array | Craigslist links |
| `urls` | array | Craigslist links (alias) |
| `maxItems` | integer | Max items |
| `fetchDetails` | boolean | Read the full posting text and attribu |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/craigslist-classifieds-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `postingId` | string |
| `postingUuid` | string |
| `title` | string |
| `url` | string |
| `price` | integer |
| `priceString` | string |
| `currency` | string |
| `categoryId` | integer |
| `categoryAbbr` | string |
| `categoryName` | string |
| `postedDate` | string |
| `cityHost` | string |
| `cityName` | string |
| `areaId` | integer |
| `subareaAbbr` | string |
| `locationDescription` | string |
| `neighborhood` | string |
| `latitude` | float |
| `longitude` | float |
| `detailLoaded` | boolean |
| `seoSlug` | string |
| `imageUrls` | list |
| `imageCount` | integer |

---

[← All scrapers](../../README.md)
