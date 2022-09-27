import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.broadwayautomotive.com/new-vehicles-green-bay-wi?make%5B%5D=Volkswagen&make%5B%5D=Chevrolet&make%5B%5D=Ford&make%5B%5D=Genesis&make%5B%5D=Hyundai&make%5B%5D=Buick&make%5B%5D=Cadillac&make%5B%5D=GMC'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')


# each set of rentals available

df = pd.DataFrame({'Title': [''], 'Description': [''], 'Price': [''], 'Link': ['']})

while True:
    postings = soup.find_all('div', class_='inventory-item clearfix js-vehicle-item')
    for i in postings:
        link = 'https://www.broadwayautomotive.com' + i.find('a', class_='js-vehicle-item-link').get('href')
        title = i.find('a', class_='vehicle-title').text
        description = i.find('div', class_='inventory-item_description_inner js-description-inner').text
        price = i.find('div', class_='price_value').text

        df = df.append({'Title': title, 'Description': description, 'Price': price, 'Link': link}, ignore_index=True)

    next_page = 'https://www.airbnb.com' + soup.find('a', {'aria-label':'Next'}).get('href')
    url = next_page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')