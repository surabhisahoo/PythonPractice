from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy_type',1)
profile.set_preference()

