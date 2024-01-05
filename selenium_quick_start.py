"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/4 15:18
@Software : PyCharm
@File     : selenium_quick_start.py
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# https://googlechromelabs.github.io/chrome-for-testing/
service = Service("chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://passport.bilibili.com/login")

time.sleep(5)
driver.close()
