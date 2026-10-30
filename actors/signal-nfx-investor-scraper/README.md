# Signal NFX Scraper

Scrape Signal NFX (signal.nfx.com) investor profiles across 32,000+ VCs, angels and scouts. Search investor lists and extract names, firms, LinkedIn, Crunchbase and X profiles; check sizes, seniority, locations, investment sectors, education and investment history.

**[Open Signal NFX Scraper on Apify](https://apify.com/abotapi/signal-nfx-investor-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~signal-nfx-investor-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "lists", "stages": ["seed"], "verticals": ["FinTech"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `stages` | array | Funding stages |
| `verticals` | array | Industries |
| `locations` | array | Locations |
| `listSlugs` | array | Specific list links |
| `searchQuery` | string | Name or firm |
| `checkSizeMin` | integer | Minimum check (USD) |
| `checkSizeMax` | integer | Maximum check (USD) |
| `positions` | array | Seniority |
| `leadOnly` | boolean | Lead investors only |
| `urls` | array | Investor, firm or list links |
| `fetchDetails` | boolean | Full investor profiles |
| `maxFundingRounds` | integer | Investment history per investor |
| `maxItems` | integer | Maximum records |
| `maxPerList` | integer | Maximum records per list |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/signal-nfx-investor-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `recordKind` | string |
| `investorProfileId` | string |
| `personSlug` | string |
| `personUrl` | string |
| `name` | string |
| `firstName` | string |
| `lastName` | string |
| `linkedinUrl` | string |
| `twitterUrl` | string |
| `crunchbaseUrl` | string |
| `angellistUrl` | string |
| `personalWebsiteUrl` | string |
| `roles` | list |
| `firstDegreeCount` | integer |
| `firmName` | string |
| `firmSlug` | string |
| `firmUrl` | string |
| `seniority` | string |
| `minCheckUsd` | integer |
| `maxCheckUsd` | integer |
| `targetCheckUsd` | integer |
| `investmentLocations` | list |
| `investorLists` | list |
| `listVertical` | string |
| `listStage` | string |
| `foundVia` | string |
| `sourceListSlug` | string |
| `scrapedAt` | string |
| `headline` | string |
| `voteCount` | integer |
| `location` | string |
| `areasOfInterestFreeform` | string |
| `degrees` | list |
| `fundingRounds` | list |
| `fundingRoundCount` | integer |
| `mediaLinks` | list |

---

[← All scrapers](../../README.md)
