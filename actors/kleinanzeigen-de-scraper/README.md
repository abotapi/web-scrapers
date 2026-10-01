# Kleinanzeigen.de Scraper

Scrape Kleinanzeigen.de ads by keyword, category, location, price, seller type, or search URL. Extract descriptions, photos, attributes, seller details, posted dates, category paths, and imprint data. Returns flat JSON records ready for spreadsheets or databases.

**[Open Kleinanzeigen.de Scraper on Apify](https://apify.com/abotapi/kleinanzeigen-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kleinanzeigen-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keyword": "fahrrad", "offerType": "any", "sellerType": "any", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keyword` | string | Keyword |
| `categoryId` | string | Category ID (optional) |
| `location` | string | Location (city or postal code, optiona |
| `radiusKm` | integer | Radius around location (km) |
| `minPrice` | integer | Min price () |
| `maxPrice` | integer | Max price () |
| `offerType` | string | Offer type |
| `sellerType` | string | Seller type |
| `sortBy` | string | Sort by |
| `urls` | array | Search URLs |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings total |
| `fetchDetails` | boolean | Fetch full ad details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kleinanzeigen-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `adId` | string |
| `url` | string |
| `title` | string |
| `descriptionShort` | string |
| `descriptionFull` | string |
| `price` | string |
| `priceAmount` | integer |
| `priceType` | string |
| `currency` | string |
| `locationText` | string |
| `postalCode` | string |
| `regionName` | string |
| `cityName` | string |
| `latitude` | null |
| `longitude` | null |
| `categoryId` | string |
| `categoryName` | string |
| `categoryPath` | string |
| `postedDate` | string |
| `postedDateText` | null |
| `viewCount` | null |
| `imageCount` | integer |
| `thumbnailUrl` | string |
| `imageUrls` | list |
| `attributes` | object |
| `attributesRaw` | list |
| `isPro` | boolean |
| `isShop` | boolean |
| `isTopAd` | boolean |
| `isSold` | boolean |
| `adType` | string |
| `tags` | list |
| `sellerId` | string |
| `sellerName` | string |
| `sellerType` | string |
| `sellerUrl` | string |
| `sellerActiveSince` | string |
| `sellerOtherAdsCount` | null |
| `imprint` | null |
| `searchUrl` | string |

---

[← All scrapers](../../README.md)
