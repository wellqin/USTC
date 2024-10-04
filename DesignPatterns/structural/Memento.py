# -*- coding:utf-8 -*-

# Memento Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 创建Memento类, 包含了要被恢复的对象的状态
class Memento:
    _state = ""

    def __init__(self, strState):
        self._state = strState

    def getState(self):
        return self._state


# 创建Originator类,创建并在 Memento 对象中存储状态
class Originator:
    _state = ""

    def setState(self, strState):
        self._state = strState

    def getState(self):
        return self._state

    def saveStateToMemento(self):
        return Memento(self._state)

    def getStateFromMemento(self, inMemento):
        self._state = inMemento.getState()


# 创建CareTaker类,Caretaker 对象负责从 Memento 中恢复对象的状态
class CareTaker:
    _mementoList = []

    def add(self, inMemento):
        self._mementoList.append(inMemento)

    def get(self, inIndex):
        return self._mementoList[inIndex]


# 调用输出,演示类使用 CareTaker 和 Originator 对象来显示对象的状态恢复
if __name__ == '__main__':
    originator = Originator()
    careTaker = CareTaker()
    originator.setState("State #1")
    originator.setState("State #2")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #3")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #4")

    print("Current State: " + originator.getState())
    originator.getStateFromMemento(careTaker.get(0))
    print("First saved State: " + originator.getState())
    originator.getStateFromMemento(careTaker.get(1))
    print("First saved State: " + originator.getState())
