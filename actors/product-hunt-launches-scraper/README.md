# Product Hunt Scraper

Extract producthunt.com data including products, launches, keyword search results, maker profiles, reviews, categories, media, social links, product websites, and optional public contact emails.

**[Open Product Hunt Scraper on Apify](https://apify.com/abotapi/product-hunt-launches-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~product-hunt-launches-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "keyword", "searchTerms": ["ai"], "searchSort": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Input mode |
| `startUrls` | array | Product Hunt URLs |
| `searchTerms` | array | Keyword search terms |
| `searchSort` | string | Keyword search sort |
| `searchCategories` | array | Keyword categories |
| `searchCategorySlugs` | array | Custom keyword category slugs |
| `enrichEmails` | boolean | Find contact emails on product website |
| `includeReviews` | boolean | Include product reviews |
| `outputReviewsAsRows` | boolean | Output reviews as separate rows |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxSearchResultsPerTerm` | integer | Max search candidates per keyword |
| `minReviewsCount` | integer | Minimum reviews |
| `minFollowersCount` | integer | Minimum followers |
| `websiteRequired` | boolean | Require product website |
| `socialLinkRequired` | boolean | Require social or source link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/product-hunt-launches-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `id` | string |
| `sourceUrl` | string |
| `canonicalUrl` | string |
| `slug` | string |
| `name` | string |
| `tagline` | string |
| `description` | string |
| `logoUrl` | string |
| `websiteUrl` | string |
| `linkedinUrl` | string |
| `twitterUrl` | string |
| `votesCount` | null |
| `commentsCount` | null |
| `followersCount` | integer |
| `reviewsCount` | integer |
| `postsCount` | integer |
| `media` | list |
| `mediaCount` | integer |
| `categories` | list |
| `reviews` | list |
| `reviewsExtracted` | integer |
| `averageRating` | float |
| `searchContext` | object |
| `scrapedAt` | string |
| `harvestedEmails` | list |

---

[← All scrapers](../../README.md)
