from selenium import webdriver
from config import config
from tkinter import messagebox

s = "BlueStar"
driver = webdriver.Chrome(executable_path=config.chromepath)
driver.maximize_window()
driver.get(config.URL)
title = driver.title
print(title)
if title == s:
    pass
else:
    driver.back()
    messagebox.showinfo("Alert", "wrong window")
