# Importing Required Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

Names = []
Desc = []
Prices = []
Reviews = [] 

# Iterating through different pages URL
for i in range(1, 21):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    # Getting HTML in Python
    r = requests.get(url)
    print(r)


    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    for name in names:
        Names.append(name.string)
    print(len(Names))

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for price in prices:
        Prices.append(price.string)
    print(len(Prices))

    descs = box.find_all("ul", class_ = "_1xgFaf")
    for desc in descs:
        Desc.append(desc.text)
    print(len(Desc))

    reviews = box.find_all("div", class_ = "_3LWZlK")
    for review in reviews:
        Reviews.append(review.text)
    print(len(Reviews))

df = pd.DataFrame({"Product Name" : Names, "Price" : Prices, "Description" : Desc, "Reviews" : Reviews})

df.to_excel("Flipkart.xlsx")