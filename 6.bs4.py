# import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/index"
response = requests.get(url)

soup = BeautifulSoup(res.text, "lmxl")
job = soup.find_all("div", class_="title")
