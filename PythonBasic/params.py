# -*- coding:utf-8 -*-


# *args 接收任意多个实际参数，并将其放到一个元组中
# 函数定义中的*args相当于打包
def print_language(*args):
    print(args)
    for a in args:
        print(a)


# 调用函数，把不同数量的参数传递进去，用位置参数
print_language('python', 'java')
print_language('python', 'java', 'php', "go")

# 函数调用时*args相当于解包
lis = ['python', 'java', 'php', "go"]
# 相当于 print_language('python', 'java', 'php', "go")
print_language(*lis)


# **kwargs 接收任意多个类似关键字参数一样显式赋值的实际参数，并将其放到一个**字典**中
# 函数定义中的**kwargs相当于打包
def print_info(**kwargs):
    print(kwargs)
    for a in kwargs.items():
        print(a)


print_info(tom=18, jack=24)
print_info(tom=18, jack=24, Aice=25)
# 函数调用时**kwargs相当于打包
di = {'cat': 18, 'jace': 24, 'alict': 65}
print_info(**di)


def foo(x=1, *args, **kwarg):
    print(args)
    print(kwarg)
    print(x)
    for item in args:
        print(item)
    for k, v in kwarg.items():
        print(k, v)
    print('*' * 50)


if __name__ == '__main__':
    print('-' * 50)
    # 1. 打包
    foo(1, 2, 3, a=4, b=5)
    foo(2, 3, a=4, b=5, c=1)

    # 2. 拆解
    v = (1, 2, 4)
    v2 = [11, 15, 23]
    d = {'a': 1, 'b': 12}
    """
    示例中如果v、v2、d没有加星号那么就当成了一个参数传递给了函数，如果加了星号那么就会解包后传递给函数。
    foo(*d, **d)等价于foo(1, 2, 4, a=1, b=12)。
    
    无论我们怎么传入参数，args都是一个tuple类型，不能进行修改。 
    对于字典类型的如果只使用一个型号*那么传入的只是字典的键。
    """
    foo(*[], **d)

    foo(1, v, d)
    foo(*v, **d)
    foo(v2, d)
    foo(*v2, **d)
