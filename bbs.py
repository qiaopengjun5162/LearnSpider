"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/3 19:09
@Software : PyCharm
@File     : bbs.py
"""
import time
import hashlib

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# 1. 北大未名 首页
response = requests.get(url="https://bbs.pku.edu.cn/v2/home.php", headers=headers)
# print(response.text)

cookie_dict = response.cookies.get_dict()
print(cookie_dict)  # {'skey': 'ea9cd3c5cf52c632', 'uid': '15265'}

# 2. 登录
username = "zhangkai"
password = "123123"
ctime = int(time.time())
data_string = f"{password}{username}{ctime}{password}"

obj = hashlib.md5()
obj.update(data_string.encode('utf-8'))
md5_string = obj.hexdigest()

response = requests.post(url="https://bbs.pku.edu.cn/v2/ajax/login.php", cookies=cookie_dict, data={
    "username": username,
    "password": password,
    "keepalive": "0",
    "time": ctime,
    "t": md5_string
})
print(response.text)  # {"success":false,"error":5}
