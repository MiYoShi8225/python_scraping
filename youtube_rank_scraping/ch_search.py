
import json
from apiclient.discovery import build
import com

API_KEY = com.api_key() ###自身で用意したAPIKeyを利用する
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
SEARCH_TEXT = 'MKR Channel'
CHANNEL_ID = "UCFOsYGDAw16cr57cCqdJdVQ"

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)

response = youtube.search().list(
    part = "snippet",
    channelId = CHANNEL_ID,
    maxResults = 2,
    order = "date" #日付順にソート
    ).execute()

for item in response.get("items", []):
    if item["id"]["kind"] != "youtube#video":
        continue
    print('*' * 10)
    print(json.dumps(item, indent=2, ensure_ascii=False))
    print('*' * 10)
