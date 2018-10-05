from selenium import webdriver
import re

l1 = []
driver = webdriver.Chrome(executable_path=r"E:\New folder\chromedriver_win32\chromedriver.exe")
driver.get("http://www.airindia.in/customer-support.htm")
source = driver.page_source
emails = re.findall(r'[\w\.-]+@[\w\d.-]+',source)

for email in emails:
    print(email)
    if email not in l1:
        l1.append(email)

print(l1)
