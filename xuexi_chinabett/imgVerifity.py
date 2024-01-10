"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/10 15:28
@Software : PyCharm
@File     : imgVerifity.py
"""
import requests
import ddddocr

res = requests.get(url="https://xuexi.chinabett.com/Login/GetValidateCode/1704871741329")
with open("code.png", mode='wb') as f:
    f.write(res.content)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)  # 1323
