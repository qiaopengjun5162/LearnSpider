"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/13 13:45
@Software : PyCharm
@File     : qunar_test.py
"""
import json
import random
import time
import base64
import binascii

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def get_slider_list():
    slider_list = []
    client_x = 300
    client_y = 500
    start_time = int(int(time.time() * 1000) % 1e5)
    width = random.randint(419, 431)
    for slice_distance in range(3, width, 26):
        if width - slice_distance <= 26:
            slice_distance = width
        start_time += random.randint(10, 1000)
        i = start_time
        o = f"{client_x + slice_distance}.00"
        u = f"{client_y + random.randint(-5, 5)}.00"
        a = f"{slice_distance}.00"
        f = f"{i};{o};{u};{a}"
        slider_list.append(f)
    return slider_list


def aes_encrypt(data_string):
    # key = "227V2xYeHTARSh1R".encode('utf-8')
    key_string = "32323756327859654854415253683152"
    key = binascii.a2b_hex(key_string)

    aes = AES.new(
        key=key,
        mode=AES.MODE_ECB
    )
    raw = pad(data_string.encode('utf-8'), 16)
    aes_bytes = aes.encrypt(raw)
    res_string = base64.b64encode(aes_bytes).decode('utf-8')
    return res_string


def run():
    res = requests.get("https://user.qunar.com/passport/login.jsp")
    cookie_dict = res.cookies.get_dict()
    cookie_qn1 = cookie_dict['QN1']

    slider_list = get_slider_list()
    slider_info = {
        "openTime": int((time.time() - random.randint(500, 3000)) * 1000),
        "startTime": int((time.time() - random.uniform(2, 4)) * 1000),
        "endTime": int((time.time() - random.uniform(0, 1)) * 1000),
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "uid": cookie_qn1,
        "track": slider_list,
        "acc": [],
        "ori": [],
        "deviceMotion": [{"isTrusted": True} for _ in range(random.randint(10, 100))]
    }

    data_string = json.dumps(slider_info, separators=(',', ':'))
    data = aes_encrypt(data_string)

    r = {
        "appCode": "register_pc",
        "cs": "pc",
        "data": data,
        "orca": 2
    }

    res = requests.post(
        url="https://vercode.qunar.com/inner/captcha/snapshot",
        json=r,
        cookies=cookie_dict
    )
    res_dict = res.json()
    slide_token = res_dict['data']["cst"]
    cookie_dict.update(res.cookies.get_dict())

    import subprocess
    res = subprocess.check_output(f'node sdk.js "{slide_token}"', shell=True)
    bella_string = res.decode('utf-8').strip()

    res = requests.post(
        url="https://user.qunar.com/weblogin/sendLoginCode",
        data={
            "usersource": "",
            "source": "",
            "ret": "",
            "ref": "",
            "business": "",
            "pid": "",
            "originChannel": "",
            "activityCode": "",
            "origin": "",
            "mobile": "17260801111",
            "prenum": "86",
            "loginSource": "1",
            "slideToken": slide_token,
            "smsType": "0",
            "appcode": "register_pc",
            "bella": bella_string,
            "captchaType": ""
        },
        cookies=cookie_dict
    )
    print(res.text)  # {"data":{"needCaptcha":true},"errcode":200,"errmsg":"success","ret":true,"ver":1}


if __name__ == '__main__':
    run()