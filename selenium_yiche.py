"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/4 21:53
@Software : PyCharm
@File     : selenium_yiche.py
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# https://googlechromelabs.github.io/chrome-for-testing/
service = Service("chromedriver-mac-arm64/chromedriver")

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-infobars")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)

opt.add_argument("--headless")

driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(service=service, options=opt)
driver.implicitly_wait(10)

driver.get("https://car.yiche.com/")

html_string = driver.page_source

soup = BeautifulSoup(html_string, features="html.parser")
tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
for tag in tag_list:
    child = tag.find(name='div', attrs={"class": "brand-name"})
    print(child.text)

driver.close()
