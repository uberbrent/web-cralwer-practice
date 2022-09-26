import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2021/REG'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table')

headers = []

th = table.find_all('th')

for i in th:
    label = i.text
    headers.append(label)

df = pd.DataFrame(columns=headers)

for j in table.find_all('tr')[1:]:
    first_td = j.find('td').find('div', class_='d3-o-club-fullname').text
    row_data = j.find_all('td')[1:]
    row = [tr.text for tr in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row

df.to_csv('/Users/uberbrent/Documents/web-scrapes/updated_nfl.csv')

