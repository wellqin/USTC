# -*- coding:utf-8 -*-

# Iterator Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 创建Iterator接口
class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass


# 创建Container接口
class Container(metaclass=ABCMeta):
    @abstractmethod
    def getIterator(self):
        pass


# 创建实现了Iterator接口的类NameIterator
class NameIterator(Iterator):
    index = 0
    aNameRepository = None

    def __init__(self, inNameRepository):
        self.aNameRepository = inNameRepository

    def hasNext(self):
        if self.index < len(self.aNameRepository.names):
            return True
        return False

    def next(self):
        if self.hasNext():
            theName = self.aNameRepository.names[self.index]
            self.index += 1
            return theName
        return None


# 创建实现了Container接口的实体类。
class NameRepository(Container):
    names = ["Robert", "John", "Julie", "Lora"]

    def getIterator(self):
        return NameIterator(self)


# 调用输出
if __name__ == '__main__':
    namesRespository = NameRepository()
    iter = namesRespository.getIterator()
    # print("Name : "+iter.aNameRepository.names[0])
    while iter.hasNext():
        strName = iter.next()
        print("Name : " + strName)
