from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get(r'http://google.com')

element = driver.find_element_by_link_text('Business')
driver.implicitly_wait(5)
element.click()
