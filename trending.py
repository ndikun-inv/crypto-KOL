import os, requests, csv, datetime

API_KEY = os.getenv("API_KEY")
url = "https://api.santiment.net/graphql"

query = """
{
  trendingWords{
    topWords{
      word
      score
    }
  }
}
"""

res = requests.post(url, json={'query': query}, headers={"Authorization": f"Bearer {API_KEY}"})
data = res.json()

utc_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
wib_now = (datetime.datetime.utcnow() + datetime.timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S")

with open("trending.csv", "a", newline="") as f:
    writer = csv.writer(f)
    for w in data["data"]["trendingWords"]["topWords"]:
        writer.writerow([utc_now, wib_now, w["word"], w["score"]])

print("Done. Saved trending.csv")
