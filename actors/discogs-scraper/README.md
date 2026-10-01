# Discogs Scraper

Scrape the Discogs catalogue by keyword, filter or link: releases, masters, artists and labels with tracklists, credits, matrix numbers, images and videos. Cross-pressing price statistics: lowest, median, highest and average asking price across an album's pressings, plus want/have demand.

**[Open Discogs Scraper on Apify](https://apify.com/abotapi/discogs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~discogs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["nirvana nevermind"], "searchType": "release", "sortBy": "relevance", "sortOrder": "desc", "maxItems": 10, "maxPages": 1, "currency": "USD", "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search keywords |
| `searchType` | string | What to return |
| `artist` | string | Artist filter |
| `label` | string | Label filter |
| `genre` | string | Genre filter |
| `style` | string | Style filter |
| `format` | string | Format filter |
| `country` | string | Country filter |
| `year` | string | Year filter |
| `catalogNumber` | string | Catalog number filter |
| `barcode` | string | Barcode filter |
| `sortBy` | string | Sort results by |
| `sortOrder` | string | Sort direction |
| `startUrls` | array | Catalogue links or ids |
| `urls` | array | Catalogue links (alias) |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max result pages per keyword |
| `fetchDetails` | boolean | Read the full record |
| `priceStats` | boolean | Price statistics across an album's pre |
| `maxPriceVersions` | integer | Pressings to price per album |
| `currency` | string | Price currency |
| `proxyConfiguration` | object | Proxy configuration |
| `discogsToken` | string | Discogs personal access token (optiona |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/discogs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `numForSale` | null |
| `lowestPrice` | null |
| `currency` | null |
| `blockedFromSale` | null |
| `marketplaceUrl` | string |
| `wantToHaveRatio` | float |
| `haveCount` | integer |
| `wantCount` | integer |
| `ratingAverage` | null |
| `ratingCount` | null |
| `priceCurrency` | null |
| `priceVersionsSampled` | null |
| `priceVersionsPriced` | null |
| `masterVersionsTotal` | null |
| `totalForSaleAcrossVersions` | null |
| `priceLowest` | null |
| `priceMedian` | null |
| `priceHighest` | null |
| `priceAverage` | null |
| `masterWantCount` | null |
| `masterHaveCount` | null |
| `masterWantToHaveRatio` | null |
| `priceSuggestionCurrency` | null |
| `priceSuggestionsRaw` | null |
| `primaryGenre` | string |
| `primaryStyle` | string |
| `primaryFormat` | string |
| `primaryLabel` | string |
| `priceSuggestionMint` | null |
| `priceSuggestionNearMint` | null |
| `priceSuggestionVeryGoodPlus` | null |
| `priceSuggestionVeryGood` | null |
| `priceSuggestionGoodPlus` | null |
| `priceSuggestionGood` | null |
| `priceSuggestionFair` | null |
| `priceSuggestionPoor` | null |
| `kind` | string |
| `recordId` | string |
| `entityId` | integer |
| `url` | string |

---

[← All scrapers](../../README.md)
