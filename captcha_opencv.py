"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/6 22:46
@Software : PyCharm
@File     : captcha_opencv.py
"""
import cv2
import numpy as np
import requests


def get_distance(bg_bytes, slice_bytes):
    def get_image_object(byte_image):
        img_buffer_np = np.frombuffer(byte_image, dtype=np.uint8)
        img_np = cv2.imdecode(img_buffer_np, 1)
        bg_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        return bg_img

    bg_image_object = get_image_object(bg_bytes)
    slice_image_object = get_image_object(slice_bytes)
    # 边缘检测
    bg_edge = cv2.Canny(bg_image_object, 255, 255)
    tp_edge = cv2.Canny(slice_image_object, 255, 255)

    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    x = max_loc[0]
    return x


# 背景图片地址
bg_image_url = "https://static.geetest.com/captcha_v4/e70fbf1d77/slide/e7874d46ba/2022-04-21T09/bg/1917b9ff568149e8a8ad82e57cf3229c.png"
# 缺口图片地址
slice_image_url = "https://static.geetest.com/captcha_v4/e70fbf1d77/slide/e7874d46ba/2022-04-21T09/slice/1917b9ff568149e8a8ad82e57cf3229c.png"

slice_bytes = requests.get(slice_image_url).content
bg_bytes = requests.get(bg_image_url).content
distance = get_distance(bg_bytes, slice_bytes)
print(distance)  # 168
