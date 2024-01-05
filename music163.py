"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/3 14:20
@Software : PyCharm
@File     : music163.py
"""
import requests
from bs4 import BeautifulSoup

headers = {
    "Referer": "https://music.163.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url="https://music.163.com/discover/playlist", headers=headers, params={"cat": "华语"})
# print("response: " + response.text)

soup = BeautifulSoup(response.text, features="html.parser")
parent_tag = soup.find(name="ul", attrs={"id": "m-pl-container"})

for child in parent_tag.find_all(recursive=False):
    title = child.find(name="a", attrs={"class": "tit f-thide s-fc0"}).text
    image_url = child.find(name="img").attrs["src"]
    print("title: " + title)
    print(f"image_url: {image_url}")

    # 下载封面
    img_res = requests.get(url=image_url)
    file_name = title.split()[0]
    with open(f"image/{file_name}.jpg", mode='wb') as f:
        f.write(img_res.content)
