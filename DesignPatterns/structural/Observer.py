# -*- coding:utf-8 -*-

# Observer Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 创建一个目标对象Subject，如果有多种不同的目标，可以抽象subject，用子对象实现
class Subject:
    # 建立一个私有集合，存放观察者对象
    _observers = []
    _state = ""

    def getState(self):
        return self._state

    def setState(self, inState):
        self._state = inState
        self.notifyAllObservers()

    # 追加观察者
    def attach(self, inObserver):
        self._observers.append(inObserver)

    # 通知观察者
    def notifyAllObservers(self):
        for aObser in self._observers:
            aObser.update()


# 创建观察者抽象类
class Observer(metaclass=ABCMeta):
    subject = Subject()

    @abstractmethod
    def update(self):
        pass

    def __init__(self):
        self.subject = Subject()


# 实现具体观察者
class BinaryObserver(Observer):
    def __init__(self, inSubject):
        self.subject = inSubject
        self.subject.attach(self)

    def update(self):
        print("Binary String : " + str(bin(self.subject.getState())))


class OctalObserver(Observer):
    def __init__(self, inSubject):
        self.subject = inSubject
        self.subject.attach(self)

    def update(self):
        print("Octal String : " + str(oct(self.subject.getState())))


class HexaObserver(Observer):
    def __init__(self, inSubject):
        self.subject = inSubject
        self.subject.attach(self)

    def update(self):
        print("Hex String : " + str(hex(self.subject.getState())))


# 调用输出
if __name__ == '__main__':
    aSubject = Subject()

    HexaObserver(aSubject)
    OctalObserver(aSubject)
    BinaryObserver(aSubject)

    print("First state change : 15")
    aSubject.setState(15)
    print("======================")
    print("First state change : 10")
    aSubject.setState(10)
