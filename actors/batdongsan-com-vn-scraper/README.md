# Batdongsan.com.vn Scraper

Scrape Batdongsan.com.vn property listings into clean JSON. Search by listing type, property category, city, or search URL. Automatically paginate results and extract prices, GPS coordinates, property specs, agent details, listing dates, and high-resolution photos.

**[Open Batdongsan.com.vn Scraper on Apify](https://apify.com/abotapi/batdongsan-com-vn-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~batdongsan-com-vn-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listingType": "Buy", "propertyType": "Apartment", "locations": ["tp-hcm"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "VN"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `listingType` | string | Buy or rent (Search mode) |
| `propertyType` | string | Property type (Search mode) |
| `locations` | array | Cities / provinces to search (Search m |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total listings |
| `fetchDetails` | boolean | Visit each listing's detail page |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/batdongsan-com-vn-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `listingType` | string |
| `propertyType` | string |
| `title` | string |
| `priceText` | string |
| `priceValue` | integer |
| `priceUnit` | string |
| `pricePerM2` | integer |
| `area` | integer |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `direction` | null |
| `balconyDirection` | null |
| `furniture` | string |
| `locationText` | string |
| `city` | string |
| `district` | string |
| `ward` | string |
| `latitude` | float |
| `longitude` | float |
| `cityCode` | string |
| `districtId` | string |
| `project` | string |
| `listingTier` | string |
| `postedDate` | string |
| `expiryDate` | string |
| `listingCode` | string |
| `agentName` | string |
| `agentId` | string |
| `agentPhone` | null |
| `agentPhoneToken` | string |
| `agentProfileUrl` | string |
| `agentAvatar` | string |
| `description` | string |
| `specs` | object |
| `imageCount` | integer |
| `images` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
