"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/10 15:13
@Software : PyCharm
@File     : py_js.py
"""
# Python 运行 JS 代码
import subprocess

res = subprocess.check_output('node demo.js "Qiao"', shell=True)
data_string = res.decode('utf-8')
print(data_string)
