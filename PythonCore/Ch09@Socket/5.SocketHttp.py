# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        5.SocketHttp
Description :   
Author :          wellqin
date:             2020/4/15
Change Activity:  2020/4/15
-------------------------------------------------
1.5、socket模拟http请求

urlparse(url)结果如下：
ParseResult(scheme='https', netloc='www.baidu.com', path='/', params='', query='', fragment='')
"""

# requests（封装了urlib） -> urlib（封装了socket） -> socket（封装TCP/UDP协议）
import socket
from urllib.parse import urlparse  # urlparse解析URL


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)
    client.connect((host, 80))  # 阻塞不会消耗cpu

    # 不停的询问连接是否建立好， 需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    """
    '\r'是回车，前者使光标到行首，不会换到下一行，如果接着输出的话，本行以前的内容会被逐一覆盖；
    '\n'是换行，后者使光标下移一格，而不会回到行首；
    对于换行这个动作，unix下一般只有一个0x0A表示换行("\n")，windows下一般都是0x0D和0x0A两个字符("\r\n")
    Enter是两个加起来的，即\r\n
    """

    data = b""  # 字符串前加b， b”“前缀代表的就是bytes
    while True:
        d = client.recv(1024)  # 依次获取1024bytes大小数据
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]  # 去除Header信息
    print(html_data)
    client.close()


if __name__ == "__main__":
    urlBaidu = "https://www.baidu.com/"
    get_url(urlBaidu)
