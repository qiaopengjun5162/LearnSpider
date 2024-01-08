"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/7 15:05
@Software : PyCharm
@File     : target_recognition.py
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

# 2.点击【滑动拼图验证】
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

# 4.等待验证码出来
time.sleep(5)

# 5.识别任务图片
target_word_list = []
parent = driver.find_element(By.CLASS_NAME, 'geetest_ques_back')
tag_list = parent.find_elements(By.TAG_NAME, "img")

for tag in tag_list:
    ocr = ddddocr.DdddOcr(show_ad=False)
    # Gets the screenshot of the current element as a binary data.
    word = ocr.classification(tag.screenshot_as_png)
    target_word_list.append(word)

print("要识别的文字：", target_word_list)

time.sleep(20)
driver.close()
