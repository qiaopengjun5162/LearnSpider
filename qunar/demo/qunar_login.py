"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/13 13:49
@Software : PyCharm
@File     : qunar_login.py
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
    mobile = input("请输入手机号：")

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
    res = requests.post(
        url="https://vercode.qunar.com/inner/captcha/snapshot",
        json={
            "appCode": "register_pc",
            "cs": "pc",
            "data": data,
            "orca": 2
        },
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
            "mobile": mobile,
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
    print(res.text)
    cookie_dict.update(res.cookies.get_dict())

    sms_code = input("请输入短信验证码：")
    res = requests.post(
        url="https://user.qunar.com/weblogin/verifyMobileVcode",
        json={
            "piccoloT": "login_register_pc",
            "mobile": mobile,
            "prenum": "86",
            "vcode": sms_code,
            "type": "3",
            "slideToken": slide_token,
            "appcode": "register_pc",
            "loginSource": 1,
            "captchaType": "",
            "source": "",
            "usersource": "",
            "ret": "",
            "ref": "",
            "business": "",
            "pid": "",
            "originChannel": "",
            "activityCode": ""
        }
    )
    cookie_dict.update(res.cookies.get_dict())

    print(res.text)
    print(cookie_dict)


if __name__ == '__main__':
    run()

"""
请输入手机号：17260801111
{"data":{"needCaptcha":true},"errcode":200,"errmsg":"success","ret":true,"ver":1}
请输入短信验证码：3586
{"ver":1,"ret":true,"errcode":200,"errmsg":"success","errkey":null,"data":{"redirect":"https://user.qunar.com/userinfo/index.jsp","needCaptcha":true,"register":"1"}}
{'QN1': '0000f78025405ac55900502b', 'JSESSIONID': 'CBC1420C4535471226353722D43F9C94', 'QN271AC': 'register_pc', 'QN271SL': '89dfe23894ac13211246121e26fb05f2', 'QN271RC': '89dfe23894ac13211246121e26fb05f2', '_i': '""', '_q': 'U.xlmlyrc2509', 'csrfToken': 'uFMWmsEfl8rkDiwHxvxvuM0dCqGeDYCq', '_s': 's_NBSKW2Z2GEFM6BL6NC2IDOLC2A', '_t': '28528192', '_v': 'T7NIE2gHcHCT8rFxeDQCk4cex9YN2VssgqoegxBnk8sjK8WNipDL6n9d4L43PmmiWSaMs2n09ZvW85I8ea3AWzsKUz3laPrQWAW-Vj44jmH-Ppu3JFwXGfcSLyo8aB7L_-qUeEyJKQcASClen6Ns9idh9lguRpRn-6fKsB5rguaC', 'QN43': '""', 'QN42': '%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7'}

"""