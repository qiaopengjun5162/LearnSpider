"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/5 20:50
@Software : PyCharm
@File     : captcha.py
"""
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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

# 1. 打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2.点击【滑动拼图验证】
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    by=By.XPATH,
    value='//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[3]'))
tag.click()

# 3. 点击开始验证
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    by=By.CLASS_NAME,
    value='geetest_btn_click'
))
tag.click()


# 4. 读取背景图片
def fetch_bg_func(dv):
    tag_object = dv.find_element(
        by=By.CLASS_NAME,
        value='geetest_bg'
    )
    style_string = tag_object.get_attribute("style")
    match_list = re.findall('url\(\"(.*)\"\);', style_string)
    if match_list:
        return match_list[0]


bg_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_bg_func)
print(f"bg_image_url: {bg_image_url}")


# 5. 读取缺口图片
def fetch_slice_func(dv):
    tag_object = dv.find_element(
        by=By.CLASS_NAME,
        value='geetest_slice_bg'
    )
    style_string = tag_object.get_attribute("style")
    match_list = re.findall('url\(\"(.*)\"\);', style_string)
    if match_list:
        return match_list[0]


slice_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_slice_func)
print(f"slice_image_url: {slice_image_url}")

time.sleep(40)
driver.close()
