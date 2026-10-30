# Vogue Scraper

Scrape Vogue fashion, beauty and culture articles with full text, runway shows, look galleries, designer archives and shopping picks with product details. Browse by channel, season or tag. Supports resume, incremental monitoring and MCP export.

**[Open Vogue Scraper on Apify](https://apify.com/abotapi/vogue-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vogue-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "articles", "channels": ["fashion", "beauty"], "searchQueries": ["handbag"], "searchSort": "relevance", "shoppingCategories": ["new-arrivals"], "productSort": "site-order", "seasons": ["spring-2027-ready-to-wear"], "designers": ["chanel", "louis-vuitton"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channels` | array | Sections |
| `searchQueries` | array | Search queries |
| `searchSort` | string | Search order |
| `shoppingCategories` | array | Shopping categories |
| `productBrands` | array | Only these brands |
| `productSort` | string | Product order |
| `seasons` | array | Seasons |
| `designers` | array | Designers |
| `startUrls` | array | Page links |
| `urls` | array | Page links (alias) |
| `fetchDetails` | boolean | Read detail pages |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max feed pages per section (0  no cap) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vogue-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `recordType` | string |
| `url` | string |
| `title` | string |
| `dek` | string |
| `summary` | null |
| `section` | string |
| `contentType` | string |
| `authors` | list |
| `authorUrls` | list |
| `pubDate` | string |
| `issueDate` | null |
| `imageUrl` | string |
| `imageAlt` | string |
| `isSponsored` | boolean |
| `subscribersOnly` | boolean |
| `videoLengthSeconds` | null |
| `functionalTags` | list |
| `sourceFeed` | string |
| `dateModified` | string |
| `imageUrls` | list |
| `keywords` | list |
| `bodyText` | string |
| `accessibleFree` | boolean |
| `inLanguage` | string |
| `thumbnailUrl` | string |
| `wordCount` | integer |
| `contentId` | string |
| `publishDate` | string |
| `modifiedDate` | string |
| `editorNames` | list |
| `sourceWordCount` | integer |
| `isCommerceContent` | boolean |
| `hasAffiliateLinks` | boolean |
| `affiliateLinksCount` | integer |
| `hasBuyButtons` | boolean |
| `templateType` | string |
| `revisions` | integer |
| `galleryImages` | integer |
| `breadcrumbs` | list |

---

[← All scrapers](../../README.md)
