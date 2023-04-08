# import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://comic.naver.com/index"
response = requests.get(url)

soup = BeautifulSoup(res.text, "lmxl")
job = soup.find_all("div", class_="title")

file_name = '202103_202103_인구현황.xlsx'
df_m = pd.read_excel(file_name, skiprows=3, index_col='행정기관', usecols='B, E:Y')
df_m
df_w = pd.read_excel(file_name, skiprows=3,
                     index_col='행정기관', usecols='B,AB:AV')
# 위에 3개만 가져와
df_m.head(3)

# string -> 숫자로 만들기 : 1,195,951 -> 1195951
df_m.iloc[0] = df_m.iloc[0].str.replace(',', '').astype(int)
df_m
