import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.yahoo.com/").text
soup = BeautifulSoup(source, "html.parser")
hotWords = soup.select("trending-list")

index = 0
for item in hotWords:
    index += 1
    print(str(index) + ", " + item.text)

    if index >= 20:
        break