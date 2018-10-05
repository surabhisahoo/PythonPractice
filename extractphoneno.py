from selenium import webdriver
import re

l1 = []
driver = webdriver.Chrome(executable_path=r"E:\New folder\chromedriver_win32\chromedriver.exe")
driver.get("http://www.airindia.in/customer-support.htm")
source = driver.page_source
phones = re.findall(r'[\d{2,3,4}- ]+[\d]+',source)

for phone in phones:
    if phone not in l1:
        l1.append(phone)

print(l1)
