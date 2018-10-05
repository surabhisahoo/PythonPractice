from selenium import webdriver

driver = webdriver.Firefox()
driver.get(r"http://google.com")
try:
    driver.find_element_by_link_text('About')
    print("test pass: element found by link text")
except:
    print("element not found")
driver.quit()