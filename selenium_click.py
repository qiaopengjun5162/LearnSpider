"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/4 18:34
@Software : PyCharm
@File     : selenium_click.py
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# https://googlechromelabs.github.io/chrome-for-testing/
service = Service("chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

# 查找元素时，没找到等待10秒去寻找，找到则继续
# driver.implicitly_wait(10)

driver.get("https://passport.bilibili.com/login")

# 1. 点击短信登录
time.sleep(3)
# 方式一
# sms_btn = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')

# 方式二
sms_btn = WebDriverWait(driver, 30, 0.5).until(
    lambda dv: dv.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'))

# 方式三
# def func(dv):
#     tag = dv.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')
#     img_src = tag.get_attribute("xxx")
#     if img_src:
#         return tag
#     return
# sms_btn = WebDriverWait(driver, 30, 0.5).until(func)

sms_btn.click()  # 点击

# 2. 输入账号
phone_txt = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input')
phone_txt.send_keys("13772324138")  # 输入

time.sleep(10)
driver.close()
