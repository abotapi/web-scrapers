# LTK Scraper

Scrape LTK (shopltk.com) creator shops by handle or URL. Extract creator profiles, posts, linked products, retailer names, rstyle affiliate links and product images. Supports recurring monitoring to track content and product changes.

**[Open LTK Scraper on Apify](https://apify.com/abotapi/shopltk-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~shopltk-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "urls", "urls": ["https://www.shopltk.com/explore/amberfillerup", "https://liketk.it/5XXza", "https://www.shopltk.com/explore/chrisellelim/posts/35cf770f-19a8-11f1-b2f3-0242ac11001a", "https://www.shopltk.com/explore/chrisellelim/collections/11f0820026ce9c87be560242ac110021", "https://www.shopltk.com/categories/salealert", "https://www.shopltk.com/categories/findsunder100", "https://www.shopltk.com/categories/findsunder50", "/search?keyword=summer+dress"], "searchQueries": ["summer dress"], "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | What to scrape |
| `urls` | array | Links to scrape |
| `searchQueries` | array | Search keywords |
| `maxItems` | integer | Max items |
| `fetchDetails` | boolean | Product details (name, price, brand, i |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/shopltk-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `kind` | string |
| `handle` | string |
| `profileId` | string |
| `displayName` | string |
| `fullName` | string |
| `instagramName` | string |
| `blogName` | string |
| `blogUrl` | string |
| `bio` | string |
| `avatarUrl` | string |
| `bgImageUrl` | null |
| `followerCount` | integer |
| `categories` | list |
| `bodyShapes` | list |
| `postCount` | integer |
| `productCount` | integer |
| `collectionCount` | integer |
| `url` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
