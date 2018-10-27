from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://coinmarketcap.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

titles = soup.find_all(class_="currency-name-container")
for i in titles:
    namelist = []
    namelist.append(i.string)
    print(namelist)

prices = soup.find_all(class_="price")
for i in prices:
    pricelist = []
    pricelist.append(i.string)
    print(pricelist)

test_df = pd.DataFrame({"Name": namelist,
                        "Price $": pricelist})

print(test_df.info())
test_df