# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        闭包
Description :   
Author :          wellqin
date:             2019/9/12
Change Activity:  2019/9/12
-------------------------------------------------
"""

"""
请大家跟我理解一下，如果在一个函数的内部定义了另一个函数，外部的我们叫他外函数，内部的我们叫他内函数。

闭包： 在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，
然后自己再结束。
"""

# 闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量


def outer(a):
    b = 10
    # inner是内函数
    def inner():
        # 在内函数中 用到了外函数的临时变量
        print(a+b)
    # 外函数的返回值是内函数的引用
    return inner


if __name__ == '__main__':
    # 在这里我们调用外函数传入参数5
    # 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
    demo()   # 15

    demo2 = outer(7)
    demo2()  # 17


"""
1 外函数返回了内函数的引用：

　　引用是什么？在python中一切都是对象，包括整型数据1，函数，其实是对象。

　　当我们进行a=1的时候，实际上在内存当中有一个地方存了值1，然后用a这个变量名存了1所在内存位置的引用。
    引用就好像c语言里的指针，大家可以把引用理解成地址。
    a只不过是一个变量名字，a里面存的是1这个数值所在的地址，就是a里面存了数值1的引用。

　　相同的道理，当我们在python中定义一个函数def demo():  的时候，内存当中会开辟一些空间，存下这个函数的代码、
    内部的局部变量等等。这个demo只不过是一个变量名字，它里面存了这个函数所在位置的引用而已。
    我们还可以进行x = demo， y = demo， 这样的操作就相当于，把demo里存的东西赋值给x和y，这样x 和y 都指向了demo函数所在的引用，
    在这之后我们可以用x() 或者 y() 来调用我们自己创建的demo() ，
    调用的实际上根本就是一个函数，x、y和demo三个变量名存了同一个函数的引用。

　　不知道大家有没有理解，很晦涩，希望我说明白了我想表达的。

　　有了上面的解释，我们可以继续说，返回内函数的引用是怎么回事了。对于闭包，在外函数outer中 最后return inner，
    我们在调用外函数 demo = outer() 的时候，outer返回了inner，inner是一个函数的引用，这个引用被存入了demo中。
    所以接下来我们再进行demo() 的时候，相当于运行了inner函数。

　　同时我们发现，一个函数，如果函数名后紧跟一对括号，相当于现在我就要调用这个函数，如果不跟括号，相当于只是一个函数的名字，
    里面存了函数所在位置的引用。

2 外函数把临时变量绑定给内函数：

　　按照我们正常的认知，一个函数结束的时候，会把自己的临时变量都释放还给内存，之后变量都不存在了。一般情况下，确实是这样的。
    但是闭包是一个特别的情况。外部函数发现，自己的临时变量会在将来的内部函数中用到，自己在结束的时候，返回内函数的同时，
    会把外函数的临时变量送给内函数绑定在一起。所以外函数已经结束了，调用内函数的时候仍然能够使用外函数的临时变量。

　　在我编写的实例中，我两次调用外部函数outer,分别传入的值是5和7。内部函数只定义了一次，我们发现调用的时候，
    内部函数是能识别外函数的临时变量是不一样的。python中一切都是对象，虽然函数我们只定义了一次，但是外函数在运行的时候，
    实际上是按照里面代码执行的，外函数里创建了一个函数，我们每次调用外函数，它都创建一个内函数，虽然代码一样，
    但是却创建了不同的对象，并且把每次传入的临时变量数值绑定给内函数，再把内函数引用返回。
    虽然内函数代码是一样的，但其实，我们每次调用外函数，都返回不同的实例对象的引用，
    他们的功能是一样的，但是它们实际上不是同一个函数对象。

 

闭包中内函数修改外函数局部变量：

　　在闭包内函数中，我们可以随意使用外函数绑定来的临时变量，但是如果我们想修改外函数临时变量数值的时候发现出问题了！
    咋回事捏？？！！（哇哇大哭）

　　在基本的python语法当中，一个函数可以随意读取全局数据，但是要修改全局数据的时候有两种方法:
    1 global 声明全局变量 2 全局变量是可变类型数据的时候可以修改

　　在闭包内函数也是类似的情况。在内函数中想修改闭包变量（外函数绑定给内函数的局部变量）的时候：
　　　　1 在python3中，可以用nonlocal 关键字声明 一个变量， 表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。
　　　　2 在python2中，没有nonlocal这个关键字，我们可以把闭包变量改成可变类型数据进行修改，比如列表。
"""

# 修改闭包变量的实例
# outer是外部函数 a和b都是外函数的临时变量


def outer(a):
    b = 10   # a和b都是闭包变量
    c = [a]  # 这里对应修改闭包变量的方法2
    # inner是内函数
    def inner():
        # 内函数中想修改闭包变量
        # 方法1 nonlocal关键字声明
        nonlocal b
        b += 1

        # 方法二，把闭包变量修改成可变数据类型 比如列表
        c[0] += 1
        print(c[0])
        print(b)
    # 外函数的返回值是内函数的引用
    return inner


if __name__ == '__main__':

    demo = outer(5)
    demo()  # 6  11   从上面代码中我们能看出来，在内函数中，分别对闭包变量进行了修改，
                     # 打印出来的结果也确实是修改之后的结果。以上两种方法就是内函数修改闭包变量的方法。

"""
还有一点需要注意：使用闭包的过程中，一旦外函数被调用一次返回了内函数的引用，虽然每次调用内函数，是开启一个函数执行过后消亡，
但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量
"""


def outer(x):
    def inner(y):
        nonlocal x
        x += y
        return x
    return inner


a = outer(10)
print(a(1))  # 11
print(a(3))  # 14 两次分别打印出11和14，由此可见，每次调用inner的时候，使用的闭包变量x实际上是同一个。


"""
闭包有啥用？？！！

　　很多伙伴很糊涂，闭包有啥用啊？？还这么难懂！

　　 3.1装饰器！！！装饰器是做什么的？？其中一个应用就是，我们工作中写了一个登录功能，我们想统计这个功能执行花了多长时间，
    我们可以用装饰器装饰这个登录模块，装饰器帮我们完成登录函数执行之前和之后取时间。

　　 3.2面向对象！！！经历了上面的分析，我们发现外函数的临时变量送给了内函数。大家回想一下类对象的情况，
    对象有好多类似的属性和方法，所以我们创建类，用类创建出来的对象都具有相同的属性方法。闭包也是实现面向对象的方法之一。
    在python当中虽然我们不这样用，在其他编程语言入比如avaScript中，经常用闭包来实现面向对象编程

　　 3.3实现单利模式！！ 其实这也是装饰器的应用。单利模式毕竟比较高大，，
    需要有一定项目经验才能理解单利模式到底是干啥用的，我们就不探讨了。
"""

