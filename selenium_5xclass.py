"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/4 15:33
@Software : PyCharm
@File     : selenium_5xclass.py
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# https://googlechromelabs.github.io/chrome-for-testing/
service = Service("chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://5xclass.cn/")

# 根据ID寻找
tag = driver.find_element(by=By.ID, value="bs-example-navbar-collapse-1")
print(tag.text)
print("--------------------------------")

# 根据类名查找
tags = driver.find_elements(by=By.CLASS_NAME, value="panel-heading")
for tag in tags:
    print(tag.text)
print("*" * 10)

# 根据标签名称查找
tags = driver.find_elements(by=By.TAG_NAME, value="li")
for tag in tags:
    print(tag.text)
print("#" * 20)

# 根据XPATH查找
tag = driver.find_element(by=By.XPATH,
                          value="/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a[1]")
print(tag.text)

# 根据XPATH查找多个
tags = driver.find_elements(by=By.XPATH,
                            value="/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a")
for tag in tags:
    print(tag.text)
print("@" * 10)

# 根据父子关系嵌套查找
parent = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div")
tags = parent.find_elements(by=By.XPATH, value="div[@class='course']/a")
for tag in tags:
    print(tag.text)

time.sleep(5)
driver.close()
