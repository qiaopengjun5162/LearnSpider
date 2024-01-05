"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/2 18:46
@Software : PyCharm
@File     : huaban.py
"""
import requests

res = requests.get(
    url="https://api.huaban.com/search/file",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    },
    params={
        "text": "美女",
        "sort": "all",
        "limit": "40",
        "page": "1",
        "position": "search_pin",
        "fields": "pins:PIN,total,facets,split_words,relations,recommend_topics",
    }
)

data_dict = res.json()
pin_list = data_dict["pins"]
for item in pin_list:
    username = item.get("user", {}).get("username")
    raw_text = item.get("raw_text")
    file_key = item.get("file", {}).get('key')
    print(f'username: {username}')
    print(f'raw_text: {raw_text}')
    print(f'file_key: {file_key}')
    img_url = f"https://gd-hbimg.huaban.com/{file_key}_fw240webp"
    img_url2 = f"https://gd-hbimg.huaban.com/{file_key}_sq75webp"
    print(f'img_url: {img_url}')
    print(f'img_url2: {img_url2}')

