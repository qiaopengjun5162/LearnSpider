"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/5 17:09
@Software : PyCharm
@File     : damai.py
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

# opt.add_argument(f"--proxy-server={proxy_string}")  # proxy server

# opt.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片

opt.add_argument("--disable-infobars")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=service, options=opt)
driver.implicitly_wait(10)

# 1.打开大麦网
driver.get('https://www.damai.cn/')

# 2.搜索框+输入 /html/body/div[1]/div/div[4]/input
tag = driver.find_element(
    By.XPATH,
    '//input[@class="input-search"]'
)
tag.send_keys("周杰伦")

# 3.点击搜索
tag = driver.find_element(
    By.XPATH,
    '//div[@class="btn-search"]'
)

tag.click()

# 4.查询列表
tag_list = driver.find_elements(
    By.XPATH,
    '//div[@class="search__itemlist"]//div[@class="items"]'
)
for tag in tag_list:
    title = tag.find_element(By.XPATH, 'div[@class="items__txt"]/div[1]/a').text
    print(title)

time.sleep(20)
driver.close()
