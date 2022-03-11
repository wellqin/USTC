# -*- coding:utf-8 -*-

def addBreaker(func):
    def inner(*args, **kwargs):
        breaker = '\n{:-^50}'
        print(breaker.format(''))
        func(*args, **kwargs)
    return inner
