# difference between __getattr__ and __getattribute__

class Count():
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi
    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0

obj1 = Count(1, 10)
print(obj1.mini)
print(obj1.maxi)
print(obj1.current)
print(obj1.hoho)