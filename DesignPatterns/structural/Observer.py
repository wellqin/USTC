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
            # 同步阻塞的实现方式: 之前讲到的实现方式，从刚刚的分类方式上来看，它是一种同步阻塞的实现方式。
            # 观察者和被观察者代码在同一个线程内执行，被观察者一直阻塞，直到所有的观察者代码都执行完成之后，才执行后续的代码。
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


"""
# 发布者基类
class Publisher:
    def __init__(self):
        self.observers = []    # 观察者们
    # 通过该方法注册一个新的观察者
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))
    # 注销一个已有的观察者
    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))
    # 在变化发生时通知所有观察者
    def notify(self):
        [o.notify(self) for o in self.observers]

# 发布者具体实现
class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name    # 设置其自己的名字，方便跟踪其状态
        self._data = 0      # 使用名称改编使其不能直接访问该变量

    # type(self).__name 是一种获取类名的方便技巧，避免硬编码类名
    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    # 提供 data 变量的读访问方式
    @property
    def data(self):
        return self._data

    # 使用了 @setter 修饰器，会在每次使用赋值操作符时被调用
    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()

# 观察者 1
class HexFormatter:
    # 通知方式有所不同
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name,hex(publisher.data)))

# 观察者 2
class BinaryFormatter:
    # 通知方式有所不同
    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,
                                                      publisher.name,bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()    
    df.add(hf)    # 关联可用的观察者
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)    # 关联可用的观察者
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()
"""
