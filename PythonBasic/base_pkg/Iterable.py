# -*- coding:utf-8 -*-
"""
    test
"""
import typing


def add_ellipsis_gen(comments: typing.Iterable[str], max_length: int = 12):
    """
    如果可迭代评论里的内容超过 max_length，剩下的字符用省略号代替
    """
    for comment in comments:
        comment = comment.strip()
        if len(comment) > max_length:
            yield comment[:max_length] + '...'
        else:
            yield comment


# 处理放在元组、列表里的评论
comments_set = ("Implementation note", "Changed", "ABC for generator")
print("\n".join(add_ellipsis_gen(comments_set)))
print("*" * 30)

comments_list = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]
print("\n".join(add_ellipsis_gen(comments_list)))

