import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.nytimes.com')
cont = page.content
soup = BeautifulSoup(cont, "html.parser")

titles = soup.find_all("h2")

with open("h2s.txt", "w+") as open_file:
    for i in titles:
        print(i.text)
        open_file.write(i.string +"\n")

