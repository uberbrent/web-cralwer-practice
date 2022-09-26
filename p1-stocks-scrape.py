import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/msft?mod=search_symbol'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# Current price and closing price
price = soup.find('div', class_='element--intraday')
current_price = price.find('bg-quote', class_='value').text
closing_price = price.find('td', class_='table__cell u-semi').text
print('Current Price: ' + current_price)
print('Closing Price: ' +  closing_price)

# High and low for 52 week average
average_div = soup.find('mw-rangebar', class_='range--yearly')
yearly_range = average_div.find_all('span', class_='primary')
yearly_low = yearly_range[0].text
yearly_high = yearly_range[1].text
print('Yearly Low: ' + yearly_low)
print('Yearly High: ' + yearly_high)

# Analyst designation on buy over sell
analyst_div = soup.find('div', class_='analyst__chart')
analyst_designation = analyst_div.find('li', class_='active').text
print('Analysis Designation: ' + analyst_designation)


