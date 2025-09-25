import requests
from datetime import datetime, timedelta, timezone
import csv

API_KEY = "API_KEY"
url = "https://api.lunarcrush.com/v2?data=market&key=" + API_KEY

res = requests.get(url)
data = res.json()

now = datetime.now(timezone.utc)
wib = now + timedelta(hours=7)

with open("trending.csv", "a", newline="") as f:
    writer = csv.writer(f)
    for coin in data.get("data", [])[:5]:  # ambil 5 coin teratas
        symbol = coin.get("s")
        print(symbol, now, wib)
        writer.writerow([symbol, now.isoformat(), wib.isoformat()])
