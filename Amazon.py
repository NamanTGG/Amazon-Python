from selenium import webdriver
from time import sleep
import time

driver=webdriver.Chrome()
driver.get('https://amazon.in')
time.sleep(5)

searchBox=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
searchBox.send_keys('Microphone')
time.sleep(5)

searchButton=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
searchButton.click()
time.sleep(5000)