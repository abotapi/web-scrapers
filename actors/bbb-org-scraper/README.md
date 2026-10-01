# BBB Scraper

Scrape bbb.org (Better Business Bureau, USA & Canada) business profiles: BBB rating, accreditation, contact and lead-gen data (decoded email, phone, website, socials, owner), address + coordinates, business type, years in business, licenses, hours, plus opt-in customer reviews and complaints..

**[Open BBB Scraper on Apify](https://apify.com/abotapi/bbb-org-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bbb-org-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["plumber"], "location": "Los Angeles, CA", "country": "USA", "sort": "Relevance", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Business terms |
| `location` | string | Location |
| `country` | string | Country |
| `sort` | string | Sort order |
| `distance` | integer | Search radius (miles) |
| `accreditedOnly` | boolean | Accredited businesses only |
| `startUrls` | array | BBB URLs |
| `maxItems` | integer | Max businesses |
| `maxPagesPerQuery` | integer | Max pages per search / URL |
| `proxy` | object | Proxy configuration |
| `scrapeReviews` | boolean | Scrape customer reviews |
| `scrapeComplaints` | boolean | Scrape complaints |
| `maxReviewPages` | integer | Max review pages per business |
| `maxComplaintPages` | integer | Max complaint pages per business |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bbb-org-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `profileUrl` | string |
| `businessId` | string |
| `bbbId` | string |
| `bbbOfficeName` | string |
| `name` | string |
| `alternateNames` | list |
| `bbbRating` | string |
| `ratingReasons` | null |
| `isAccredited` | boolean |
| `accreditedDate` | string |
| `bbbFileOpenedDate` | string |
| `phone` | string |
| `additionalPhones` | null |
| `faxNumbers` | null |
| `email` | string |
| `additionalEmails` | list |
| `website` | string |
| `ownerName` | string |
| `ownerTitle` | string |
| `streetAddress` | string |
| `addressLine2` | null |
| `city` | string |
| `stateCode` | string |
| `zipCode` | string |
| `formattedAddress` | string |
| `countryCode` | string |
| `latitude` | float |
| `longitude` | float |
| `serviceAreas` | list |
| `yearsInBusiness` | integer |
| `businessStartDate` | string |
| `incorporatedDate` | string |
| `businessType` | string |
| `entityType` | string |
| `numberOfEmployees` | null |
| `isOutOfBusiness` | boolean |
| `description` | string |
| `paymentMethods` | null |
| `licenses` | list |
| `primaryCategory` | string |

---

[← All scrapers](../../README.md)
