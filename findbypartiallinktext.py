from selenium import webdriver

driver = webdriver.Firefox()
driver.get(r"https://www.wikipedia.org/")
try:
    driver.find_element_by_partial_link_text('Terms')
    print('test pass: partial link found')
except:
    print("element not found")
driver.quit()