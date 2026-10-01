# iProperty MY Scraper

Scrape property listings from iProperty.com.my for sale or rent: price, PSF, bedrooms, bathrooms, floor area, tenure, property type, full address, agent (name, license, agency, contact numbers) and photo gallery. Search and URL modes, filters, 6 sort orders, and optional detail enrichment.

**[Open iProperty MY Scraper on Apify](https://apify.com/abotapi/iproperty-com-my-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~iproperty-com-my-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "channel": "sale", "location": "Kuala Lumpur", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "MY"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channel` | string | Channel |
| `location` | string | Location |
| `propertyType` | string | Property type |
| `priceMin` | integer | Minimum price (MYR) |
| `priceMax` | integer | Maximum price (MYR) |
| `bedrooms` | integer | Minimum bedrooms |
| `sortBy` | string | Sort by |
| `urls` | array | iProperty.com.my URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/iproperty-com-my-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `listingId` | integer |
| `externalId` | null |
| `url` | string |
| `listingUrl` | string |
| `searchUrl` | string |
| `title` | string |
| `propertyType` | string |
| `propertyTypeGroup` | string |
| `typeText` | string |
| `statusCode` | string |
| `price` | object |
| `priceValue` | integer |
| `pricePretty` | string |
| `priceType` | null |
| `pricePerArea` | string |
| `psf` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `floorArea` | integer |
| `areaText` | string |
| `tenure` | string |
| `location` | object |
| `fullAddress` | string |
| `shortAddress` | string |
| `agent` | object |
| `agency` | object |
| `agentRating` | object |
| `images` | list |
| `imageCount` | integer |
| `thumbnail` | string |
| `badges` | list |
| `postedOn` | object |
| `recency` | string |
| `developer` | string |
| `isVerified` | boolean |
| `isOfficialListing` | boolean |
| `isDeveloperListing` | boolean |
| `newProject` | boolean |
| `projectId` | integer |

---

[← All scrapers](../../README.md)
