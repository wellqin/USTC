# -*- coding:utf-8 -*-


# Proxy Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 定义Image接口
class Image(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


# 实现Image的实体类：RealImage，ProxyImage类
class RealImage(Image):
    _strFilename = ""

    def __init__(self, inFilename):
        self._strFilename = inFilename
        self.loadFromDisk(inFilename)

    def display(self):
        print("Displaying " + self._strFilename)

    def loadFromDisk(self, inFilename):
        print("Loadng " + inFilename)


class ProxyImage(Image):
    _realImage = None
    _strFilename = ""

    def __init__(self, inFilename):
        self._strFilename = inFilename

    def display(self):
        if self._realImage is None:
            self._realImage = RealImage(self._strFilename)
        self._realImage.display()


# 调用输出
if __name__ == '__main__':
    aImage = ProxyImage("test_10mb.jpg")
    # 图片将从磁盘加载
    aImage.display()
    print("")
    # 图片不需要从磁盘加载
    aImage.display()
