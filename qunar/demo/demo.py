"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/13 12:49
@Software : PyCharm
@File     : demo.py
"""
import subprocess

res = subprocess.check_output("node sdk.js '15cf502c3128593b1a3237e5c484d6c9'", shell=True)
data_string = res.decode("utf-8")
print(data_string)
