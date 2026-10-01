# Doc To Markdown MCP Server Scraper

An MCP server that converts documents to clean Markdown. Convert PDFs, Word docs, Excel spreadsheets, PowerPoints, HTML, images, and more to AI-friendly Markdown format.

**[Open Doc To Markdown MCP Server Scraper on Apify](https://apify.com/abotapi/doc-to-markdown-mcp?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~doc-to-markdown-mcp/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"defaultHeadingStyle": "atx"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `defaultIncludeMetadata` | boolean | Include Metadata by Default |
| `defaultIncludeToc` | boolean | Include TOC by Default |
| `defaultHeadingStyle` | string | Default Heading Style |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/doc-to-markdown-mcp?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).


---

[← All scrapers](../../README.md)
