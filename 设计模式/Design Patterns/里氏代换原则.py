# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        里氏代换原则
Description :   
Author :          wellqin
date:             2020/4/5
Change Activity:  2020/4/5
-------------------------------------------------
"""


"""
简单地说，基类存在的地方，子类是可以替换的。

软件中将一个基类对象替换成它的子类对象，程序将不会产生任何错误和异常，反过来则不成立。
所以在程序中尽量使用基类类型定义对象，在运行时再确定其子类类型，用子类对象来替换父类对象。

里氏替换是继承复用的基础，只有当派生类可以替换掉基类，基类才能真正被复用，而派生类才能够在基类基础上增加新的功能。
LSP是对开闭原则(关键是抽象化)的补充。

里氏替换的重点在不影响父类中的原功能。父类中除了未实现的抽象方法外，就是已经实现好的方法，
这些已实现好的方法实际上是一系列设定好的规范和约定，如果子类对这些非抽象已实现好的方法任意修改，
就会对整个继承复用造成破坏。
"""


"""
以枪战片中警察抓坏蛋为例，已实现Gun抽象类及HandGun和MachineGun两个子类，现新需求增加一个玩具手枪，
但是玩具手枪又不能用来射击杀人，所以不能直接扩展为Gun抽象类的子类，
选择的解决方案是另外创建一个抽象类Toy通过委托模式跟Gun抽象类建立代理关系，
Toy抽象类的子类ToyGun可以自由扩展自己的行为。
"""


class Gun(object):
    def __init__(self, name="枪", shape="Gun Shape", sound="Ping Ping"):
        self.name = name
        self.shape = shape
        self.sound = sound

    def shoot(self):
        pass


class Handgun(Gun):
    def __init__(self, name="手枪"):
        super(Handgun, self).__init__(name)

    def shoot(self):
        print("掏出{}，开始射击...".format(self.name))


class MachineGun(Gun):
    def __init__(self, name="机枪"):
        super(MachineGun, self).__init__(name)

    def shoot(self):
        print("架好{}，开始射击...".format(self.name))


class Police(object):
    def __init__(self, gun):
        self.__gun = gun

    def kill_badman(self):
        print("警察开始杀坏人...")
        self.__gun.shoot()


if __name__ == '__main__':
    police = Police(Handgun())
    police.kill_badman()


















