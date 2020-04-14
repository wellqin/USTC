# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        6.BigFile
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

1.6、生成器如何读取大文件
当在工作中，应用生成器提取大文件（一行大文件）。
"""


# 大文件, 只有一行,数据间以分隔符“{|}”隔开
def MyReadLines(file, newline):
    buf = ""  # 设置空的缓存区
    while True:
        # 第一次进入buf为空，直接跳到下面读取文件
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]  # 提交第一行
            buf = buf[pos + len(newline):]  # 将提交出去的舍弃掉
        chunk = file.read(4096)

        if not chunk:
            # 说明已经读到了文件结尾，然后将buf提交出去
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    for line in MyReadLines(f, "{|}"):
        print(line)


