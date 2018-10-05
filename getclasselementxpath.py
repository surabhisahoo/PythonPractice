from selenium import webdriver

driver = webdriver.Firefox()
driver.get(r'http://google.com')
id = driver.find_elements_by_xpath('//*[@class]')
for i in id:
    print(i.get_attribute('class'))

driver.quit()