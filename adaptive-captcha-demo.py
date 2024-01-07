"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/7 14:34
@Software : PyCharm
@File     : adaptive-captcha-demo.py
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

service = Service("chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)

# 1.打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2.点击【滑动拼图验证】
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[3]'
))
tag.click()

# 3.点击开始验证
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.CLASS_NAME,
    'geetest_btn_click'
))
tag.click()


# 4.读取背景图片
def fetch_image_func(class_name):
    def inner(dv):
        tag_object = dv.find_element(
            By.CLASS_NAME,
            class_name
        )
        style_string = tag_object.get_attribute("style")
        match_list = re.findall('url\(\"(.*)\"\);', style_string)
        if match_list:
            return match_list[0]

    return inner


bg_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_image_func("geetest_bg"))
slice_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_image_func("geetest_slice_bg"))

slice_bytes = requests.get(slice_image_url).content
bg_bytes = requests.get(bg_image_url).content

slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
res = slide.slide_match(slice_bytes, bg_bytes, simple_target=True)
x1, y1, x2, y2 = res['target']
print("滑动距离", x1)


def show_func(dv):
    geetest_box_tag = dv.find_element(By.CLASS_NAME, "geetest_box")
    display_string = geetest_box_tag.get_attribute("style")
    if "block" in display_string:
        time.sleep(2)
        return dv.find_element(By.CLASS_NAME, 'geetest_btn')


btn_tag = WebDriverWait(driver, 30, 0.5).until(show_func)

ActionChains(driver).click_and_hold(btn_tag).perform()  # 点击并抓住标签
ActionChains(driver).move_by_offset(xoffset=x1, yoffset=0).perform()  # 向右滑动103像素（向左是负数）
ActionChains(driver).release().perform()

time.sleep(200)
driver.close()
