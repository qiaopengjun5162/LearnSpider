"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/6 22:41
@Software : PyCharm
@File     : captcha_ddddocr.py
"""
import ddddocr
import requests

# 背景图片地址
bg_image_url = "https://static.geetest.com/captcha_v4/e70fbf1d77/slide/e7874d46ba/2022-04-21T09/bg/1917b9ff568149e8a8ad82e57cf3229c.png"
# 缺口图片地址
slice_image_url = "https://static.geetest.com/captcha_v4/e70fbf1d77/slide/e7874d46ba/2022-04-21T09/slice/1917b9ff568149e8a8ad82e57cf3229c.png"

slice_bytes = requests.get(slice_image_url).content
bg_bytes = requests.get(bg_image_url).content

slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
res = slide.slide_match(slice_bytes, bg_bytes, simple_target=True)
x1, y1, x2, y2 = res['target']
print(x1, y1, x2, y2)  # 168 110 248 190
