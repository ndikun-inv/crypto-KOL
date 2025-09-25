import os
import requests

API_KEY = os.getenv("SENTIMENT_API_KEY")

url = "https://api.santiment.net/graphql"

query = """
{
  getTrendingWords {
    word
    score
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

    if "data" in data and "getTrendingWords" in data["data"]:
        for item in data["data"]["getTrendingWords"]:
            print(f"{item['word']} - score: {item['score']}")
    else:
        print("No data returned, check query or API key.")
else:
    print("Error:", response.status_code, response.text)
