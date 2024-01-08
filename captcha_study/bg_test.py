"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/8 15:15
@Software : PyCharm
@File     : bg_test.py
"""
# @课程   : 爬虫逆向实战课
# @讲师   : 武沛齐
# @课件获取: wupeiqi666

import re
import time
import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from PIL import Image, ImageDraw
from io import BytesIO

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
    word = ocr.classification(tag.screenshot_as_png)
    target_word_list.append(word)

print("要识别的文字：", target_word_list)  # ['尝', '酥', '饼']

# 6.背景图片
bg_tag = driver.find_element(
    By.CLASS_NAME,
    'geetest_bg'
)
content = bg_tag.screenshot_as_png

# 7.识别背景中的所有文字并获取坐标
ocr = ddddocr.DdddOcr(show_ad=False, det=True)
poses = ocr.detection(content)  # [(x1, y1, x2, y2), (x1, y1, x2, y2), x1, y1, x2, y2]
print(f"poses: {poses}")  #  [[23, 78, 76, 130], [20, 16, 75, 70]]

# 8.循环坐标中的每个文字并识别
bg_word_dict = {}
img = Image.open(BytesIO(content))

for box in poses:
    x1, y1, x2, y2 = box
    # 根据坐标获取每个文字的图片
    corp = img.crop(box)
    img_byte = BytesIO()
    corp.save(img_byte, 'png')
    # 识别文字
    ocr2 = ddddocr.DdddOcr(show_ad=False)
    word = ocr2.classification(img_byte.getvalue())  # 识别率低

    # 获取每个字的坐标  {"鸭":}
    bg_word_dict[word] = [int((x1 + x2) / 2), int((y1 + y2) / 2)]

print(bg_word_dict)  # {'尝': [49, 104], '酥': [47, 43]}

time.sleep(10)
driver.close()
