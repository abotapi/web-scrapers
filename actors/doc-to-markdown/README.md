# Doc To Markdown Scraper

Convert documents (PDF, Word, PowerPoint, Excel, HTML, images) to clean Markdown. Supports batch processing, metadata extraction, and customizable output formatting.

**[Open Doc To Markdown Scraper on Apify](https://apify.com/abotapi/doc-to-markdown?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~doc-to-markdown/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"urls": ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"], "headingStyle": "atx", "outputFormat": "both"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `files` | array | Upload Files |
| `urls` | array | URLs |
| `includeMetadata` | boolean | Include Metadata |
| `includeToc` | boolean | Generate Table of Contents |
| `headingStyle` | string | Heading Style |
| `outputFormat` | string | Output Format |
| `memoryMbytes` | integer | Memory (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/doc-to-markdown?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `filename` | string |
| `success` | boolean |
| `error` | null |
| `format` | string |
| `size_bytes` | integer |
| `conversion_time_ms` | integer |
| `markdown` | string |
| `metadata` | object |

---

[← All scrapers](../../README.md)
