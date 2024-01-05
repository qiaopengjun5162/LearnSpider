"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/3 22:29
@Software : PyCharm
@File     : ruanwen.py
"""
import requests
import ddddocr  # pip install ddddocr

headers = {
    "Referer": "https://i.ruanwen.la/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.post(url="https://api.ruanwen.la/api/auth/captcha/generate", headers=headers)
res_dict = response.json()

print("response: ", res_dict)
captcha_token = res_dict.get('data', {}).get('captcha_token')
captcha_src = res_dict.get('data', {}).get('src')

res = requests.get(url=captcha_src)
# with open(f"{captcha_token}.png", mode='wb') as f:
#     f.write(res.content)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(f"code: {code}")

# 登录认证
res = requests.post(url="https://api.ruanwen.la/api/auth/authenticate",
                    json={"mobile": "13772923138", "device": "pc", "password": "123424",
                          "captcha_token": captcha_token, "captcha": code,
                          "identity": "advertiser"})
response = res.json()
print(response)
# {'success': False, 'message': '账号不存在', 'status': 200}
