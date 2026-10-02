# GoWork FR & DE Company Reviews and Profile Scraper

Extract company profiles from GoWork France and Germany, including contact details, review threads with replies, ratings breakdowns, opening hours, social links, SIREN/NAF identifiers, and 100+ structured company fields. Supports keyword search, URL input, and bulk sitemap discovery.

**[Open GoWork FR & DE Company Reviews and Profile Scraper on Apify](https://apify.com/abotapi/gowork-eu-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gowork-eu-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locale": "fr", "queries": ["Carrefour"], "sitemapKind": "constant", "output": "company", "maxPages": 1, "maxListings": 10, "maxReviewsPerCompany": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "FR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start mode |
| `locale` | string | Site locale |
| `queries` | array | Search queries |
| `urls` | array | Start URLs |
| `sitemapKind` | string | Sitemap kind |
| `sitemapFilter` | string | Sitemap URL keyword filter (optional) |
| `output` | string | Output shape |
| `fetchDetails` | boolean | Fetch full company detail (recommended |
| `maxPages` | integer | Max SERP pages per search |
| `maxListings` | integer | Max companies (hard cap across all mod |
| `maxReviewsPerCompany` | integer | Max review threads per company |
| `minRating` | integer | Minimum company rating |
| `minReviewCount` | integer | Minimum review count |
| `ratedOnly` | boolean | Only companies with at least one rated |
| `verifiedOnly` | boolean | Only verified companies |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gowork-eu-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `source` | string |
| `listingId` | string |
| `slug` | string |
| `url` | string |
| `statusCode` | integer |
| `siteLocale` | string |
| `scrapedAt` | string |
| `pageTitle` | string |
| `metaDescription` | string |
| `ogTitle` | string |
| `ogDescription` | string |
| `ogImage` | string |
| `ogUrl` | string |
| `canonicalUrl` | string |
| `h1` | string |
| `htmlLang` | string |
| `reviewCountFromTitle` | integer |
| `jsonLd` | list |
| `isUpstreamChallenge` | boolean |
| `parseMeta` | object |
| `companyId` | string |
| `org_name` | string |
| `longName` | string |
| `altName` | string |
| `status` | integer |
| `dataStatus` | integer |
| `flagsBits` | list |
| `multiCity` | boolean |
| `companyEmail` | null |
| `companyPhone` | string |
| `org_telephone` | string |
| `companyWebsite` | string |
| `companyWebsiteRaw` | string |
| `companyWebpageTitle` | null |
| `companyWebpageDescription` | null |
| `companyLinkedInUrl` | null |
| `companyInstagramUrl` | null |
| `companyFacebookUrl` | string |
| `companyTwitterUrl` | null |
| `companyYouTubeUrl` | null |

---

[← All scrapers](../../README.md)
