# Mediator Pattern with Python Code
from abc import abstractmethod, ABCMeta
import time


# 创建中介类ChatRoom
class ChatRoom:
    @staticmethod
    def showMessage(inUser, inMessage):
        locTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("{0} [{1}] : {2}".format(locTime, inUser.getName(), inMessage))


# 创建User类
class User:
    _name = ""

    def __init__(self, inName):
        self._name = inName

    def getName(self):
        return self._name

    def setName(self, inName):
        self._name = inName

    def sendMessage(self, inMessage):
        ChatRoom.showMessage(self, inMessage)


# 调用输出
if __name__ == '__main__':
    robert = User("Robert")
    john = User("John")
    robert.sendMessage("Hi, John!")
    john.sendMessage("Hello,Robert!")
