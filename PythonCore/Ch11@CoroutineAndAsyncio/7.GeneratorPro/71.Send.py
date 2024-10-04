# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        7.GeneratorPro
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------

六. 生成器的send和yield from
    1.生成器send和next方法：

        启动生成器方式有两种：1.next()；2.send()；

        生成器可以产出值；也可以接收值（调用方传递进来的值）；

        send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield的位置
        注：在调用send()发送非none之前，我们必须启动一次生成器，否则会抛错，方式有两种gen.send(None)或者next(gen)

"""


def gen_func():
    # 注意：html = yield XXX
    # 1. 生成器可以产出值；XXX
    # 2. 也可以接收值（调用方传递进来的值）；html
    # 所以如果只是接受值的话，html = yield 即可，不需要XXX
    html = yield 'https://www.baidu.com'
    print(html)
    yield 1
    yield 2
    return 'QW'


if __name__ == '__main__':
    gen = gen_func()
    # 启动生成器方式有两种：1.next()；2.send()；
    # print(next(gen))

    # 注：在调用send()发送非none之前，我们必须启动一次生成器，否则会抛错，方式有两种gen.send(None)或者next(gen)
    url = gen.send(None)
    # url = next(gen)

    html = "qw"
    # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield的位置
    gen.send(html)
    print(gen.send(html))  # 2
