"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/3 10:22
@Software : PyCharm
@File     : yiche.py
"""
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://car.yiche.com/")
# print(f"Response: %s" % response.text)

soup = BeautifulSoup(response.text, features="html.parser")
# tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
# # print(f"Tag list: %s" % tag_list)
#
# for tag in tag_list:
#     tag_name = tag.attrs["data-name"]
#     print(f"Tag name: %s" % tag_name)

tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
for tag in tag_list:
    child = tag.find(name="div", attrs={"class": "brand-name"})
    child_text = child.text
    print(f"child_text: %s" % child_text)