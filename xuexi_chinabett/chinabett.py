"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/10 23:02
@Software : PyCharm
@File     : chinabett.py
"""
import execjs
import requests
import ddddocr
from bs4 import BeautifulSoup

# 1.首页请求
cookie_dict = {}
res = requests.get(url="https://xuexi.chinabett.com/")
cookie_dict.update(res.cookies.get_dict())
print(f"cookie_dict: {cookie_dict}")

# 2.获取验证码地址
soup = BeautifulSoup(res.text, features="html.parser")
image_tag = soup.find(name="img", attrs={"id": "imgVerifity"})
code_src = image_tag.attrs['src']
print(f"code src: {code_src}")

# 3.读取验证码并实现
res = requests.get(url=f"https://xuexi.chinabett.com{code_src}", cookies=cookie_dict)
cookie_dict.update(res.cookies.get_dict())
ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(f"code: {code}")

# 4.处理用户名&密码
with open(file="encry_base64.js", mode="r") as f:
    js_string = f.read()

JS = execjs.compile(js_string)

# 用户名
username = JS.call("base64encode", "137723245123")
# 密码
temp = JS.call("base64encode", "123123")
password = JS.call("encrypt_pwd", temp)

# 5.登录
res = requests.post(
    url="https://xuexi.chinabett.com/Login/Entry",
    data={
        "userAccount": username,
        "password": password,
        "returnUrl": "/PersonalCenter",
        "proVing": code,
    },
    cookies=cookie_dict
)
print(res.text)
