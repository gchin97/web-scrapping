import requests

res = requests.get("http://google.com")
# res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
