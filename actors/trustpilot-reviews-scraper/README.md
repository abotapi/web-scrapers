# Trustpilot Scraper

Scrape Trustpilot business profiles and reviews on any country domain: TrustScore, the exact 1-5 star distribution in counts and percentages, reply rate, claim and verification status, contact block, plus reviews with verification badge and company reply. Keyword, category sweep or pasted links.

**[Open Trustpilot Scraper on Apify](https://apify.com/abotapi/trustpilot-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~trustpilot-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchType": "keyword", "query": "bookshop.org", "category": "book_store", "site": "www.trustpilot.com", "maxReviewsPerBusiness": 10, "reviewLanguage": "all", "reviewSort": "recency", "reviewsSince": "any", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchType` | string | Search type |
| `query` | string | Search query |
| `category` | string | Category id |
| `urls` | array | Trustpilot links or company domains |
| `site` | string | Trustpilot country domain |
| `scrapeReviews` | boolean | Scrape reviews |
| `maxReviewsPerBusiness` | integer | Max reviews per business |
| `reviewStars` | array | Star ratings |
| `reviewLanguage` | string | Review language |
| `reviewSort` | string | Review order |
| `verifiedOnly` | boolean | Verified reviews only |
| `reviewsSince` | string | Review age |
| `reviewKeyword` | string | Review keyword |
| `fetchDetails` | boolean | Fetch business details |
| `minTrustScore` | integer | Minimum TrustScore |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/trustpilot-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `businessId` | string |
| `identifyingName` | string |
| `displayName` | string |
| `profileUrl` | string |
| `websiteUrl` | string |
| `websiteTitle` | string |
| `logoUrl` | string |
| `trustScore` | float |
| `stars` | integer |
| `numberOfReviews` | integer |
| `numberOfReviewsLast12Months` | integer |
| `reviewsMatchingFilters` | integer |
| `reviewsInSelectedLanguages` | integer |
| `ratingDistribution` | object |
| `ratingDistributionPercent` | object |
| `ratingDistributionTotal` | integer |
| `negativeReviewShare` | float |
| `positiveReviewShare` | float |
| `reviewLanguages` | list |
| `hasMultipleLanguages` | boolean |
| `isClaimed` | boolean |
| `isClosed` | boolean |
| `isTemporarilyClosed` | boolean |
| `isCollectingReviews` | boolean |
| `hasCollectedIncentivisedReviews` | boolean |
| `isUsingPaidFeatures` | boolean |
| `isUsingAIResponses` | boolean |
| `claimedDate` | string |
| `verifiedByGoogle` | boolean |
| `verifiedPaymentMethod` | boolean |
| `verifiedUserIdentity` | boolean |
| `replyPercentage` | float |
| `averageDaysToReply` | float |
| `negativeReviewsWithRepliesCount` | integer |
| `totalNegativeReviewsCount` | integer |
| `lastReplyToNegativeReview` | string |
| `primaryCategoryId` | string |
| `primaryCategoryName` | string |

---

[← All scrapers](../../README.md)
