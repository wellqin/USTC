# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        11.WithStatement
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------

2.1、python中的with语句
"""


# try  except  else  finally
def exe_try():
    try:
        print("coding is started")
        raise KeyError  # 主动抛出KeyError
    except KeyError as e:
        print("key error")
        return 2
    except IndexError as e:  # 不断添加异常判断，可能有很多，就会造成代码冗长，那么可以简化吗？
        print("Index error")
        return 22
    else:  # 要程序没有出异常就会运行else，上面的出异常就不会执行
        print("other coding")
        return 3
    finally:  # 不管前面怎样，都会执行
        print("finally")
        return 4  # 注释掉则代码返回2


"""
    coding is started
    key error
    finally
    4  # 为什么是4，在Error中返回的2，22怎么没打印出来呢？【异常处理在堆栈中，最后返回的是栈顶元素】
"""


# python会自动识别自己的协议
# 上下文管理器协议(with调用)（简化try-finally用法的）
class Sample:
    def __enter__(self):
        # 获取资源
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def doSomething(self):
        print("do something")


with Sample() as sample:
    sample.doSomething()
    """
    当我们进入with语句的时候，就会调用__enter__方法
    当我们离开with语句的时候，就会调用__exit__方法
    
    运行结果：
    enter
    do something
    exit
    """

if __name__ == '__main__':
    result = exe_try()
    print(result)
    """
    运行结果：为什么会出现这样的结果？程序运行，直接抛出异常KeyError先返回2进入栈底（栈的知识），
    然后执行finally中的返回4，4进入栈顶，栈的规则是后进先出，则返回的是4
    coding is started
    key error
    finally
    4
    """
