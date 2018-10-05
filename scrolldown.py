from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get(r"http://wikipedia.org")
#scroll down and up
elem = driver.find_element_by_tag_name('html')
elem.send_keys(Keys.END)
time.sleep(4)
elem.send_keys(Keys.HOME)

#get browser version
print(driver.capabilities['version'])

#get current URL
print(driver.current_url)

#open URL in new tab
ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get(r"http://bing.com")
#switch to new tab
time.sleep(3)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
time.sleep(3)
driver.find_element_by_tag_name(ele).send_keys(Keys.CONTROL + 'W')


#maximize window
driver.maximize_window()
print(driver.get_window_size())
driver.set_window_size(1024,768)
print(driver.get_window_size())

#get source file
print(driver.page_source)


