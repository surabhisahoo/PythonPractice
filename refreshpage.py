from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get(r"http://wikipedia.org")

time.sleep(2)
#refreshing the page
driver.refresh()
#to go back

driver.back()

#forward
driver.forward()