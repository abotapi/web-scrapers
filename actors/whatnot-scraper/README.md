# Whatnot Scraper

Scrape Whatnot live and upcoming shows, queued items and lots, and seller profiles. Search by keyword or URL, then filter by category, format, seller rating, and country. Extract ratings, followers, sold counts, and more.

**[Open Whatnot Scraper on Apify](https://apify.com/abotapi/whatnot-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~whatnot-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "resultType": "shows", "queries": ["charizard"], "categories": ["pokemon_cards"], "minSellerRating": "any", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `resultType` | string | Result type |
| `queries` | array | Search keywords |
| `urls` | array | Whatnot links |
| `categories` | array | Categories |
| `showStatus` | array | Time of show (live shows only) |
| `showFormat` | array | Show format (live shows only) |
| `buyingFormat` | array | Buying format (items and lots only) |
| `conditions` | array | Condition (items and lots only) |
| `gradedOnly` | boolean | Graded only (items and lots only) |
| `autographedOnly` | boolean | Autographed only (items and lots only) |
| `minSellerRating` | string | Minimum seller rating |
| `premierShopOnly` | boolean | Premier shops only |
| `sellerCountries` | array | Seller country |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `sortBy` | string | Sort by |
| `fetchSellerDetails` | boolean | Read each seller's full profile |
| `maxSellerReviews` | integer | Reviews per seller |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/whatnot-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `showId` | string |
| `url` | string |
| `title` | string |
| `description` | null |
| `status` | string |
| `isLiveNow` | boolean |
| `isScheduled` | boolean |
| `startTime` | string |
| `endTime` | null |
| `activeViewers` | integer |
| `watchlistUsers` | integer |
| `isHiddenBySeller` | boolean |
| `categories` | list |
| `categorySlugs` | list |
| `tags` | list |
| `showLabels` | list |
| `isFreeShippingEnabled` | null |
| `buyerMaxShippingCost` | null |
| `currency` | null |
| `thumbnailUrl` | string |
| `trailerUrl` | null |
| `searchMode` | string |
| `searchQuery` | string |
| `scrapedAt` | string |
| `sellerId` | string |
| `sellerUsername` | string |
| `sellerUrl` | string |
| `sellerIsLive` | boolean |
| `sellerIsVerified` | boolean |
| `sellerIsPremierShop` | null |
| `sellerFollowerCount` | integer |
| `sellerSoldCount` | integer |
| `sellerRating` | float |
| `sellerReviewCount` | integer |
| `sellerProfileImageUrl` | string |

---

[← All scrapers](../../README.md)
