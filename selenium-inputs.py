from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = '/Users/uberbrent/Documents/ChromeDriver/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com/imghp?hl=en&ogbl')

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys('Lucy Edgerunners')

box.send_keys(Keys.ENTER)

# box.send_keys(Keys.ENTER) -- for pressing enter after typing in text to search bar
# Gathering screenshots of html elements
#for i in range(1, 10):
   # driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('/Users/uberbrent/Documents/web-scrapes/screenshot'+str(i)+'.png')


height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    newHeight = driver.execute_script('return document.body.scrollHeight')
    if height == newHeight:
        break
    height = newHeight
