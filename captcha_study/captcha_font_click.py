"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/7 14:43
@Software : PyCharm
@File     : captcha_font_click.py
"""
import re
import time
import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

service = Service("../chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

# 1.打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2.点击【文字点选验证】
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[4]'
))
tag.click()

# 3.点击开始验证
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.CLASS_NAME,
    'geetest_btn_click'
))
tag.click()

time.sleep(5)

# 要识别的目标图片
target_tag = driver.find_element(
    By.CLASS_NAME,
    'geetest_ques_back'
)
target_tag.screenshot("target.png")

# 识别图片
bg_tag = driver.find_element(
    By.CLASS_NAME,
    'geetest_bg'
)
bg_tag.screenshot("bg.png")

time.sleep(20)
driver.close()
