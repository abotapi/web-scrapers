"""YouTube Transcript & Subtitle Scraper: minimal example. Docs: https://apify.com/abotapi/youtube-transcript-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/youtube-transcript-scraper").call(
    run_input={
        "mode": "url",
        "videoUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://youtu.be/dQw4w9WgXcQ", "https://m.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/shorts/jNQXAC9IVRw", "https://www.youtube.com/live/IoL51xLkMSY", "https://www.youtube.com/embed/dQw4w9WgXcQ", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI", "https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI", "https://www.youtube.com/@YouTube", "https://www.youtube.com/@YouTube/videos", "https://www.youtube.com/channel/UCBR8-60-B28hp2BmDPdntcQ", "https://www.youtube.com/user/YouTube", "https://www.youtube.com/c/YouTubeCreators", "https://www.youtube.com/results?search_query=python+tutorial"],
        "searchQueries": ["python tutorial"],
        "maxVideos": 10,
        "languages": ["en"],
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
