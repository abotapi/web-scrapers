# BetaList Scraper

Scrape BetaList.com startup profiles with founder and contact enrichment. Extract startup names, taglines, descriptions, topics, regions, images, websites, social links, public emails, phone numbers, and founder details.

**[Open BetaList Scraper on Apify](https://apify.com/abotapi/betalist-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~betalist-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["ai"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `topic` | string | Topic |
| `region` | string | Region |
| `boostedOnly` | boolean | Boosted startups only |
| `featuredAfter` | string | Featured on or after |
| `featuredBefore` | string | Featured on or before |
| `urls` | array | BetaList URLs |
| `fetchDetails` | boolean | Fetch detail pages |
| `getContacts` | boolean | Enrich with contacts |
| `maxItems` | integer | Max startups |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/betalist-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `record_type` | string |
| `id` | integer |
| `startup_id` | integer |
| `url` | string |
| `slug` | string |
| `title` | string |
| `name` | string |
| `one_liner` | string |
| `short_description` | string |
| `description` | string |
| `visit_url` | string |
| `website_url` | string |
| `website_domain` | string |
| `boosted` | boolean |
| `featured_at` | string |
| `featured_date_label` | string |
| `topics` | list |
| `topic_names` | list |
| `image_urls` | list |
| `primary_image_url` | string |
| `logo_url` | string |
| `regions` | list |
| `similar_startups` | list |
| `contacts` | null |
| `contacts_lookup_url` | string |
| `source` | object |

---

[← All scrapers](../../README.md)
