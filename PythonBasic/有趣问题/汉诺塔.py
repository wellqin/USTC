# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        汉诺塔
Description :   
Author :          wellqin
date:             2019/9/8
Change Activity:  2019/9/8
-------------------------------------------------
"""

#!python2
# -*- coding: utf-8 -*-
# 用turtle动画效果演示汉诺塔的移动过程

# import turtle
# import time
# from random import randrange
#
# def move_tower(height, fromPole=-1, toPole=1, withPole=0, speed=3):
#     turtle_list = []
#     pole_distance = 200
#     pole_bottom = -150
#     pole_len = 300
#     pole_size = 20
#
#     # 递归调用的主逻辑
#     def main_logic(height, fromPole, toPole, withPole):
#         if height >= 1:
#             main_logic(height - 1, fromPole, withPole, toPole)
#             move_disk(fromPole, toPole)
#             main_logic(height - 1, withPole, toPole, fromPole)
#
#     # 移动单个盘子
#     def move_disk(fp, tp):
#         for i in range(height - 1, -1, -1):
#             if turtle_list[i].pos()[0] == fp * pole_distance:
#                 animation(turtle_list[i], fp, tp)
#                 return
#
#     # 产生移动单个盘子的动画效果
#     def animation(t, fp, tp):
#         t.up()
#         t.speed(speed)
#         t.goto(fp * pole_distance, pole_bottom + pole_len + 30)
#         t.goto(tp * pole_distance, pole_bottom + pole_len + 30)
#         num = -1
#         for tx in turtle_list:
#             if tx.pos()[0] == tp * pole_distance:
#                 num = num + 1
#         t.goto(tp * pole_distance, pole_bottom + (num + 0.5) * 21)
#
#     # 初始化动画场景
#     def init(height):
#
#         # 定义函数绘制一根柱子
#         def draw_pole(t, pos):
#             t.up()
#             t.goto(pos[0] - pole_size / 2.0, pos[1])
#             t.down()
#             t.setheading(90)
#             t.pensize(1)
#             t.begin_fill()
#             for i in range(2):
#                 t.forward(pole_len)
#                 t.right(90)
#                 t.forward(pole_size)
#                 t.right(90)
#             t.end_fill()
#
#         # 绘制底线和三根柱子
#         t = turtle.Turtle()
#         t.hideturtle()
#         w.tracer(3)
#         t.pensize(4)
#         t.color('#a9a9a9')
#         t.up()
#         t.goto(-400, pole_bottom - 3)
#         t.down()
#         t.goto(400, pole_bottom - 3)
#         draw_pole(t, pos=(-pole_distance, pole_bottom))
#         draw_pole(t, pos=(0, pole_bottom))
#         draw_pole(t, pos=(pole_distance, pole_bottom))
#         t.hideturtle()
#
#         # 生成所要求数量的盘子
#         for i in range(height):
#             t = turtle.Turtle()
#             t.hideturtle()
#             t.seth(90)
#             w.colormode(255)
#             t.color((randrange(256),randrange(256),randrange(256)))
#             t.shape('square')
#             t.shapesize((height - i) * 1 + 1, 1)
#             t.up()
#             t.goto(-pole_distance, pole_bottom + (i + 0.5) * 21)
#             t.showturtle()
#             turtle_list.append(t)
#         w.tracer(1)
#
#     # 当函数被调用时，先初始化场景，随后开始移动盘子
#     init(height)
#     time.sleep(1)
#     main_logic(height, fromPole, toPole, withPole)
#
# # 主程序
# num_of_disk = input('Please input the number of disks:')
# speed = None
# temp = input('Do you want to set animation speed?(y/n):')
# if temp in 'yY':
#     speed = input('Please input the speed(1--10 and the fastest 0):')
#
# # 整个函数在单击画布时被执行
# def main(x, y):
#     w.onclick(None)
#     move_tower(num_of_disk, speed=speed)
#
# w = turtle.Screen()
# print('Now please click on the canvas!')
# w.onclick(main)
# turtle.mainloop()

"""
把n个盘子从a移到c，借助中介b。这个操作记为move(n, a, b, c)

因为一次只能移动一个，那么最先做的就是把最下面的移到c,所以需要把n-1个都移到b(此时中介是c)。因此有一步move(n-1, a, c, b)

现在，可以把那一块最大的从a直接移动到c了。然后，a没有，b有n-1个，c有一个(最大的)。现在的目标就是把n-1个盘子从b移动到c了，中介是a。
参考最上面的写法，这个就是move(n-1, b, a, c)

总结一下:如何移动呢？先把n-1个放中间，最大的拿过去，再把n-1个拿过去，只不过位置参数变了。
每次调用两个递归，复杂度是指数级别


"""


def move(n, a, b, c):       # 把n个盘子从a移到c，借助中介b。这个操作记为move(n, a, b, c)
    if n == 1:
        print(a, '-->', c)
        return
    else:
        move(n-1, a, c, b)  # 首先需要把 (N-1) 个圆盘移动到 b
        move(1, a, b, c)    # 将a的最后一个圆盘移动到c
        move(n-1, b, a, c)  # 再将b的(N-1)个圆盘移动到c


move(4, 'A', 'B', 'C')
