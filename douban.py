"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/2 19:13
@Software : PyCharm
@File     : douban.py
"""
import requests


def get_spider_data(url: str, params: dict) -> dict:
    return requests.get(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        },
        params=params
    ).json()


request_url = "https://movie.douban.com/j/search_subjects"
request_params = {
    "type": "movie",
    "tag": "豆瓣高分",
    "page_limit": "50",
    "page_start": "0",
}
res = get_spider_data(url=request_url, params=request_params)
subjects = res.get('subjects')
for subject in subjects:
    movie_title = subject.get('title')
    movie_url = subject.get('url')
    movie_cover = subject.get('cover')
    print(f"title: {movie_title}")
    print(f"url: {movie_url}")
