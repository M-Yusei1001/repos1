import requests
from bs4 import BeautifulSoup
import re

print("取得したいYahooニュース記事のURLをペーストしてください")
url = input(">")

#HTMLの取得
response = requests.get(url)

#文字化け防止
response.encoding = response.apparent_encoding

#BeautifulSoupオブジェクト作成
soup = BeautifulSoup(response.content, "html.parser")

with open("article.txt", "w", encoding="utf-8") as f:
    #要素の抽出
    items = soup.find_all(re.compile("article"))

    for item in items:
        f.write(item.text)

print("スクレイピングは正常に終了しました")        
    