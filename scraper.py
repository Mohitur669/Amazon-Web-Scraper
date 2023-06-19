# Importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# url from searching "playstation 5" in amazon.in
URL = "https://www.amazon.in/s?k=playstation+5&sprefix=pla%2Caps%2C464&ref=nb_sb_ss_ts-doa-p_1_3"

# to tell the website that we are not a bot we need to pass headers (using user-agent)
HEADERS = {
    "User-Agent": "your user agent",
    "Accept-Language": "en-US, en;q=0.5",
}

# making request to the website
webpage = requests.get(URL, headers=HEADERS, timeout=10)

# checking connection
print(webpage.status_code)  # 200 means request is successful

# printing the content of the webpage
print(webpage.content)  # but it gives response in bytes format

# Now we need to use BeautifulSoup to parse the content of the webpage
soup = BeautifulSoup(webpage.content, "html.parser")

# find different links in the webpage
links = soup.find_all(
    "a",
    class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal",
)

# print the links
print(links[0].get("href"))  # but the links are not complete

# Now we need to concatenate the base url with the links
link = links[0].get("href")
product_list = "https://www.amazon.in" + link
print(product_list)

# Now we need to make request to the product page, We are doing this do get all products links in future
new_webpage = requests.get(product_list, headers=HEADERS, timeout=10)

# checking connection
print(new_webpage.status_code)  # 200 means request is successful

# printing the content of the webpage
new_soup = BeautifulSoup(new_webpage.content, "html.parser")
print(new_soup)

# Now we need to find the title of the product
title = new_soup.find("span", attrs={"id": 'productTitle'}).text.strip()
print(title)

# Now we need to find the price of the product
new_soup.find(
    "span",
    attrs={
        "class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"
    },
)

# but above code output contains duplicate price, to solve
new_soup.find("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"}, ).find(
    "span", attrs={"class": "a-offscreen"}).text

# Now we need to find the rating of the product
new_soup.find("span", attrs={"class": "a-icon-alt"}).text