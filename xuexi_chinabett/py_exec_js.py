"""
@Project  : LearnSpider
@Author   : QiaoPengjun
@Time     : 2024/1/10 15:20
@Software : PyCharm
@File     : py_exec_js.py
"""
# python  -> pyexecjs  -> node.js  -> javascript
import execjs

js_string = """
function func(arg) {
    return arg + ' World!';
}
"""
JS = execjs.compile(js_string)

sign = JS.call("func", "Hello")
print(sign)
