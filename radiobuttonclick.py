import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get(r'https://www.zkoss.org/zkdemo/input/radio_button')
for i in driver.find_elements_by_xpath("//*[@type='radio']"):
    i.click()

time.sleep(3)