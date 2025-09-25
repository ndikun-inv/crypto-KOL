import os
import requests

API_KEY = os.getenv("SENTIMENT_API_KEY")

url = "https://api.lunarcrush.com/graphql"

query = """
{
  getTrendingWords {
    word
    score
    volume
    social_volume
  }
}
"""

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, json={"query": query}, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("RAW RESPONSE:", data)

    # kalau mau cuma list kata trending
    words = data["data"]["getTrendingWords"]
    for w in words:
        print(f"{w['word']} - score: {w['score']} - volume: {w['volume']}")
else:
    print("Error:", response.status_code, response.text)
