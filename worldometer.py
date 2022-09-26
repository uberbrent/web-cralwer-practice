import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# table
pop_table = soup.find('table')

th = pop_table.find_all('th')
headers = []
for i in th:
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns=headers)

for j in pop_table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row

df.to_csv('/Users/uberbrent/Documents/wordstats.csv')

