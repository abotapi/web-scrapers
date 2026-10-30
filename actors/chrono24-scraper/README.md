# Chrono24 Scraper

Scrape Chrono24 luxury watch listings by keyword, filters or URL. Extract 50+ fields including brand, model, reference number, price, year, condition, movement, case specifications, seller details, location, images and more.

**[Open Chrono24 Scraper on Apify](https://apify.com/abotapi/chrono24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~chrono24-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQuery": "Rolex Submariner", "sortBy": "relevance", "maxReviewsPerListing": 10, "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQuery` | string | Search keyword |
| `searchParams` | object | Filters |
| `manufacturerIds` | string | Brand ids |
| `catalogCollectionId` | string | Catalog collection id |
| `catalogModelId` | string | Catalog model id |
| `priceFrom` | integer | Min price |
| `priceTo` | integer | Max price |
| `watchTypes` | string | New or used |
| `condition` | string | Condition code |
| `certified` | boolean | Certified only |
| `specials` | array | Delivery contents |
| `movementTypes` | string | Movement type |
| `gender` | string | Gender |
| `caseDiameter` | string | Case diameter (mm) |
| `year` | string | Year |
| `waterproof` | string | Water resistance code |
| `functions` | array | Functions |
| `styles` | array | Styles |
| `caseMaterials` | array | Case materials |
| `dialColor` | array | Dial colors |
| `braceletMaterial` | array | Bracelet materials |
| `braceletColor` | array | Bracelet colors |
| `sellerType` | string | Seller type |
| `stockInfo` | string | Stock |
| `countryIds` | string | Seller countries |
| `trackingId` | string | Tracking id |
| `sortBy` | string | Sort by |
| `dealsOnly` | boolean | Top Deals collection only |
| `urls` | array | Start URLs |
| `fetchDetails` | boolean | Fetch full details |
| `fetchSellerReviews` | boolean | Include seller reviews |
| `maxReviewsPerListing` | integer | Max reviews per listing |
| `flatten` | boolean | Flatten specs |
| `includeRaw` | boolean | Include raw size marker |
| `maxListings` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/chrono24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `listingId` | string |
| `watchId` | string |
| `listingUrl` | string |
| `sourceUrl` | string |
| `title` | string |
| `brand` | string |
| `model` | string |
| `referenceNumber` | string |
| `listingCode` | string |
| `description` | string |
| `price` | integer |
| `priceDisplay` | string |
| `currency` | string |
| `availability` | string |
| `availabilityText` | string |
| `condition` | string |
| `conditionText` | string |
| `year` | string |
| `location` | string |
| `sellerCountry` | string |
| `sellerUsername` | string |
| `merchantCountry` | null |
| `certificationStatus` | string |
| `isDeal` | boolean |
| `scopeOfDelivery` | string |
| `gender` | string |
| `productType` | string |
| `marketingType` | string |
| `collectionId` | integer |
| `modelId` | integer |
| `modelVariantId` | integer |
| `refId` | integer |
| `buyingAgent` | null |
| `specs` | object |
| `images` | list |
| `thumbnail` | string |
| `mainImage` | string |
| `imageUrls` | list |
| `certifiedStatus` | string |

---

[← All scrapers](../../README.md)
