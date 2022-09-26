import requests
from bs4 import BeautifulSoup

# url of website we are going to scrape
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

# set the page variable to be the entire html
page = requests.get(url)

# prettifying the html to be human-readable and parseable
soup = BeautifulSoup(page.text, 'lxml')

# find functionality for BeautifulSoup
# grabbing the first element with the header tag
soup.find('header')

# grabbing the first div with class of container test-site
soup.find('div', {'class': 'container test-site'})

# grabbing the first h4 with the class of pull-right price
soup.find('h4', {'class': 'pull-right price'})

# general find_all functionality for
# finding all h4 elements with the class pull-right price
prices = soup.find_all('h4', {'class': 'pull-right price'})

# for loop to print out the array
# for p in prices:
#    print(p.text)

# more specific find_all functions

# finding elements based on boolean
soup.find_all(id = True)

# finding strings in the html
soup.find_all(string = 'Iphone')

import re

# find all strings including Iph
soup.find_all(string = re.compile('Iph'))

# pull all classes containing the string pull
soup.find_all(class_=re.compile('pull'))

# find all from a specific tag with the class string, limit parameter available
pull = soup.find_all('p', class_=re.compile('pull'), limit = 3)

# full table of all information on test site
product_name = soup.find_all('a', class_=re.compile('title'))
prices = soup.find_all('h4', class_=re.compile('price'))
reviews = soup.find_all('p', class_=re.compile('pull-right'))
descriptions = soup.find_all('p', class_=re.compile('description'))

product_name_list = []
price_list = []
reviews_list = []
description_list = []

for i in product_name:
    name = i.text
    product_name_list.append(name)

for i in prices:
    price = i.text
    price_list.append(price)

for i in reviews:
    review = i.text
    reviews_list.append(review)

for i in descriptions:
    description = i.text
    description_list.append(description)

import pandas as pd

table = pd.DataFrame({'Product Name':product_name_list, 'Description':description_list,
                      'Price':price_list, 'Reviews':reviews_list})

# selecting parent divs for faster parsing
boxes = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
print(len(boxes))

