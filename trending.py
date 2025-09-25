import os, requests, datetime

API_KEY = os.getenv("SENTIMENT_API_KEY")
url = "https://api.santiment.net/graphql"

query = """
{
  trendingWords {
    topWords {
      word
      score
    }
  }
}
"""

headers = {"Authorization": f"Apikey {API_KEY}"}
response = requests.post(url, json={"query": query}, headers=headers)

print("RAW RESPONSE:", response.text)  # <-- DEBUG CETAK ISI RESPON

data = response.json()

if "data" not in data:
    print("Error dari API:", data)
    exit(1)

utc_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
wib_now = (datetime.datetime.utcnow() + datetime.timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S")

print(f"UTC: {utc_now}, WIB: {wib_now}")

for w in data["data"]["trendingWords"]["topWords"]:
    print(f"{w['word']} | Score: {w['score']}")
