from selenium import webdriver

driver = webdriver.Firefox()
driver.get(r"http://google.com")

try:
    driver.find_element_by_xpath("//a[@class='_Gs']")
    print('test Pass: found')
except:
    print("element not fouund")

driver.quit()