# TrustMate.io Scraper

Scrape complete company review histories from TrustMate.io. Paste company profile URLs, slugs, or domains, with support for both Polish `/opinie/` and English `/reviews/` profiles. Extract one row per review, including rating, full review text, author, date, and company details.

**[Open TrustMate.io Scraper on Apify](https://apify.com/abotapi/trustmate-io-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~trustmate-io-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "minRating": "1", "sortBy": "newest", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `companyUrls` | array | Company URLs, slugs or domains |
| `startUrls` | array | Company profile URLs / slugs / domains |
| `minRating` | string | Minimum rating |
| `sortBy` | string | Sort reviews by |
| `maxItems` | integer | Max items |
| `maxPagesPerCompany` | integer | Max review pages per company |
| `includeTranslations` | boolean | Include machine translations |
| `fetchDetails` | boolean | Fetch company profile enrichment |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/trustmate-io-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `platform` | string |
| `reviewId` | integer |
| `reviewPublicId` | string |
| `rating` | integer |
| `reviewBody` | string |
| `authorName` | string |
| `authorType` | string |
| `reviewWeight` | integer |
| `reviewDate` | string |
| `reviewUpdatedAt` | string |
| `language` | string |
| `verified` | boolean |
| `notVerified` | boolean |
| `companyReply` | string |
| `companyReplyDate` | string |
| `companyReplyUpdatedAt` | string |
| `companyResponseTimeHours` | float |
| `helpfulCount` | integer |
| `unhelpfulCount` | integer |
| `pinned` | boolean |
| `shared` | boolean |
| `imported` | boolean |
| `importSource` | null |
| `orderIdentifier` | string |
| `orderNumber` | null |
| `isOrderLinked` | boolean |
| `reviewStatus` | integer |
| `reviewEnabled` | boolean |
| `mediationExists` | boolean |
| `issuedAtLocation` | boolean |
| `binaryQuestionAnswers` | list |
| `translations` | list |
| `companyName` | string |
| `companySlug` | string |
| `companyWebsite` | string |
| `companyCategory` | string |
| `companyAccountId` | integer |
| `companyVerified` | boolean |
| `companyEmail` | string |
| `companyNip` | string |

---

[← All scrapers](../../README.md)
