from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = '/Users/uberbrent/Documents/ChromeDriver/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.goat.com/sneakers')
for i in range(1, 10):
    price = driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div/span').text
    print(price)