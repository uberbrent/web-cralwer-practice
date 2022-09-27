import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# needed info
# link, name, price, color

df = pd.DataFrame({'Name': [''], 'Price': [''], 'Color': [''], 'Link': ['']})
x = 0

while x < 15:
    entries = soup.find_all('div', class_= 'media soft push-none rule')
    for i in entries:
        data = i.find('div', class_= 'media__content')
        name = data.find('a').text
        price = data.find('strong', class_= 'delta').text
        color = data.find_all('div', class_= 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        link = 'https://www.carpages.ca' + i.find('a', class_= 'media__img media__img--thumb').get('href')

        df = df.append({'Name': name, 'Price': price, 'Color': color, 'Link': link}, ignore_index=True)

    url = 'https://www.carpages.ca' + soup.find('a', {'title': 'Next Page'}).get('href')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    x = x + 1

df.to_csv('/Users/uberbrent/Documents/web-scrapes/cars.csv')

