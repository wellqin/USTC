# -*- coding:utf-8 -*-

"""
https://github.com/joerick/pyinstrument
pyinstrument是一款python性能分析器，它通过记录程序执行过程中的堆栈记录来帮你找出程序最耗时的代码。
pyinstrument每1毫秒中断一次程序，并在那一点记录整个堆栈，单个函数的执行时长会在函数执行结束后被记录。
当你的python程序性能需要优化时，可以考虑使用pyinstrument来定位程序慢在哪里。
"""

import requests
from pyinstrument import Profiler


"""
pyinstrument开发人员给了一份配合flask使用的示例代码

from flask import Flask, g, make_response, request
app = Flask(__name__)

@app.before_request
def before_request():
    if "profile" in request.args:
        g.profiler = Profiler()
        g.profiler.start()


@app.after_request
def after_request(response):
    if not hasattr(g, "profiler"):
        return response
    g.profiler.stop()
    output_html = g.profiler.output_html()
    return make_response(output_html)
    
before_request 会在视图处理请求前执行，after_request会在请求得到处理后返回结果前执行，如果请求的参数里包含了profile参数，
表示需要记录整个调用栈的信息，当请求得到响应后，会调用output_html方法得到一个html页面，并将其返回，作者给的这个例子非常使用，
但只适用于get请求，在浏览器里发出get请求，加入profile参数，就可以在浏览器里得到整个调用过程中调用堆栈的信息。
"""

def test_api():
    url = 'http://www.coolpython.net'
    res = requests.get(url)
    print(res.status_code)


profiler = Profiler()

profiler.start()
test_api()
profiler.stop()

print(profiler.output_text(unicode=True, color=True))
