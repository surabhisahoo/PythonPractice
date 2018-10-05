import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get(r'http://demos.dojotoolkit.org/dijit/tests/form/test_CheckBox.html')

for i in range(20):
    try:
        driver.find_element_by_xpath("//*[contains(text(),'cb7: normal checkbox')]").click()

    except NoSuchElementException:
        print("retry again")




