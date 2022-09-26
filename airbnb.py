import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.com/s/Tokyo--Japan/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&date_picker_type=calendar&checkin=2022-10-01&checkout=2022-10-31&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=7&query=Tokyo%2C%20Japan&place_id=ChIJ51cu8IcbXWARiRtXIothAS4'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

while True:
    postings = soup.find_all('div', class_='c4mnd4m')
    for i in postings:
        link = 'https://www.airbnb.com' + i.find('a', class_='ln2bl2p dir dir-ltr').get('href')
        print(link)
        info = soup.find('div', class_='g1tup9az')
        name = info.find('div', class_='t1jojoys')

    next_page = 'https://www.airbnb.com' + soup.find('a', {'aria-label':'Next'}).get('href')
    url = next_page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')