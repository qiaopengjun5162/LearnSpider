"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/2 20:33
@Software : PyCharm
@File     : ke_qq.py
"""
import requests

url = "https://ke.qq.com/cgi-proxy/course_list/search_course_list?bkn=&r=0.0346"

headers = {
    "Referer": "https://ke.qq.com/course/list?page=2",
    "Content-Type": "application/json;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

data = {"page": "2", "visitor_id": "32438328905040303", "finger_id": "caeb36a7c27bb921ef746e01e796709d", "platform": 3,
        "source": "search", "count": 24, "need_filter_contact_labels": 1}

response = requests.post(url=url, headers=headers, json=data).json()
result = response.get('result')
search_result = result.get('search_result')
for item in search_result:
    course = item.get('course')
    name = course.get('name')
    cover_url = course.get('cover_url')
    content_desc = course.get('content_desc')
    print(f"{name} \n{cover_url} \n{content_desc}")
