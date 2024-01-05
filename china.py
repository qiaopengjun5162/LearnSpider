"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/3 18:19
@Software : PyCharm
@File     : china.py
"""
import requests
from bs4 import BeautifulSoup

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://passport.china.com/logon",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# response = requests.post(url="https://passport.china.com/logon", headers=headers, data={
#     "userName": "18630087660",
#     "password": "qwe123456",
# })
# cookie_dict = response.cookies.get_dict()
# print(response.text)
# print(cookie_dict)

cookie_dict = {'nickname': 'china_4880gpuk16789969', 'lastlogindate': '2024-01-03', 'lastlogintime': '"18:28:03"',
               'lastloginip': '117.23.99.32', 'bindMobile': '"1@186*****660"',
               'CHINACOMID': '742c958c-4995-48ef-8d20-0075fb75c3540',
               'CP_USER': 'FKBo6w-aaDEfuWahi2uiM3GsUTKrctp4zIpsuaQNIsJMLwh1DirMwoPMx5oiyf8wkhih3KHukIe9qQVNNdpoo%2FVd9argTa42%2FB2Ut-0nAmb306rHCJYjyV0OyXoHzv3z5Ft7cWGKOa00sROAco1ePtsPivkjVy53p9KJ38gG0edGLtdEpbmPWObBaXLwuQwPB9Rpu7LYNLnPN2s42HGHr4U5Z3P-HtfhmlLJ6WjemIAiC44IuLq2ow%3D%3D',
               'CP_USERINFO': '4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D',
               'china_variable': 'jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza',
               'SESSION_COOKIE': '128'}

response = requests.get(url="https://passport.china.com/main", cookies=cookie_dict)

# print(response.text)
soup = BeautifulSoup(response.text, features="html.parser")
# tag = soup.find(name="p", attrs={"id": "usernick"}).text
tag = soup.find(attrs={"id": "usernick"})
print(tag.text)
title = tag.attrs['title']
print(title)