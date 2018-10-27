from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
soup = bs(r.content, "html.parser")

data1 = soup.find_all("div", {"class:", "dek"})

for item in data1:
    print(item.text)

data2 = soup.find_all("section", {"class:", "content-section"})

for item in data2:
    print(item.text)

