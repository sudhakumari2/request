import requests
from bs4 import BeautifulSoup
url=requests.get("https://webscraper.io/test-sites")
data=BeautifulSoup(url.text,"html.parser")
Div=data.find_all("div",class_="container test-sites")
for d1 in Div:
    a1=d1.find_all("h2",class_="site-heading")
    # print(a1)
    for i in a1:
        print(i.text)
        