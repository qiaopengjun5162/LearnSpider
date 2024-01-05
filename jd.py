"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/5 15:39
@Software : PyCharm
@File     : jd.py
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

# 1. 打开京东
driver.get("https://www.jd.com/")

tag = driver.find_element(by=By.XPATH, value='//*[@id="ttbar-login"]/a[1]/span[2]')
tag.click()
tag = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[2]/div[1]/div/div/div[2]/div[1]/a')
tag.click()

# 2. 搜索框+输入
tag = driver.find_element(by=By.XPATH, value='//*[@id="key"]')
tag.send_keys("iphone手机")

# 3. 点击搜索
tag = driver.find_element(by=By.XPATH, value='//*[@id="search"]/div/div[2]/button')
tag.click()

# 4. 查询列表
tag_list = driver.find_elements(by=By.XPATH, value='//*[@id="J_goodsList"]/ul/li')

for index, tag in enumerate(tag_list):
    title = driver.find_element(by=By.XPATH, value=f'//*[@id="J_goodsList"]/ul/li[{index+1}]/div/div[4]/a/em').text
    print(f"title: {title}")

time.sleep(3)
driver.close()


