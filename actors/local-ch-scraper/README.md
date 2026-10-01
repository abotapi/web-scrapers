# Local.ch Scraper

Pull structured company data from local.ch, including name, address, GPS, phone, email, website, hours, ratings, social links, photos, and categories. Search by category and location or use URLs. Supports Deutsch, English, Français, and Italiano.

**[Open Local.ch Scraper on Apify](https://apify.com/abotapi/local-ch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~local-ch-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "restaurant", "where": "zurich", "language": "de", "maxPages": 1, "maxListings": 10, "maxReviewsPerListing": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "CH"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Run mode |
| `reviewOnly` | boolean | Review-only output |
| `category` | string | Category (single) |
| `queries` | array | Categories (multi) |
| `where` | string | Location |
| `language` | string | Language |
| `urls` | array | local.ch URLs |
| `maxPages` | integer | Maximum pages per search |
| `maxListings` | integer | Maximum rows (0  unlimited) |
| `fetchDetails` | boolean | Fetch detail pages |
| `includeReviews` | boolean | Include review comments |
| `maxReviewsPerListing` | integer | Maximum reviews per listing |
| `maxReviewRows` | integer | Maximum review rows |
| `maxConcurrency` | integer | Max concurrent detail requests (no lon |
| `ratedOnly` | boolean | Only listings with ratings |
| `minRating` | integer | Minimum rating |
| `withPhone` | boolean | Only listings with a phone number |
| `withEmail` | boolean | Only listings with an email address |
| `withWebsite` | boolean | Only listings with a website |
| `premiumOnly` | boolean | Only premium-listed companies |
| `matchQueryPostalCode` | boolean | Only listings matching the query posta |
| `skipRegionalFallback` | boolean | Only listings from exact query matches |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/local-ch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `name` | string |
| `subtitle` | string |
| `language` | string |
| `entryType` | string |
| `schemaOrgType` | string |
| `isPremium` | boolean |
| `favorited` | boolean |
| `professionalTitle` | null |
| `address` | string |
| `street` | string |
| `zipCode` | string |
| `city` | string |
| `canton` | string |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `phone` | string |
| `phoneAlt` | null |
| `mobile` | null |
| `fax` | null |
| `email` | string |
| `emailAlt` | null |
| `website` | string |
| `whatsapp` | null |
| `facebook` | string |
| `instagram` | string |
| `linkedin` | null |
| `twitter` | null |
| `tiktok` | null |
| `pinterest` | null |
| `youtube` | null |
| `xing` | null |
| `foursquare` | null |
| `mainCategory` | string |
| `mainCategorySlug` | string |
| `categories` | list |
| `categorySlugs` | list |
| `rating` | integer |
| `ratingCount` | integer |

---

[← All scrapers](../../README.md)
