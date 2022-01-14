# -*- coding:utf-8 -*-


from abc import abstractmethod, ABCMeta


# 创建一个表示食物条目和食物包装的接口
class Item(metaclass=ABCMeta):
    @abstractmethod
    def myName(self):
        pass

    @abstractmethod
    def packing(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Packing(metaclass=ABCMeta):
    @abstractmethod
    def pack(self):
        pass


# 实现Packing接口的实体类
class Wrapper(Packing):
    def pack(self):
        return "Wrapper"


class Bottle(Packing):
    def pack(self):
        return "Bottle"


# 实现Item接口的抽象类
class Burger(Item):
    def packing(self):
        return Wrapper()

    @abstractmethod
    def price(self):
        pass


class ColdDrink(Item):
    def packing(self):
        return Bottle()

    @abstractmethod
    def price(self):
        pass


# 创建扩展了Burger和ColdDrink的实体类
class VegBurger(Burger):
    def price(self):
        return 25.0

    def myName(self):
        return "Veg Burger"


class ChickenBurger(Burger):
    def price(self):
        return 50.5

    def myName(self):
        return "Chicken Burger"


class Coke(ColdDrink):
    def price(self):
        return 30.0

    def myName(self):
        return "Coke"


class Pepsi(ColdDrink):
    def price(self):
        return 35.0

    def myName(self):
        return "Pepsi"


# 设计一个Meal类，带有上面定义的对象
class Meal:
    __items = []

    # 注意初始化，否则类变量会被重用
    def __init__(self):
        self.__items = []

    def addItem(self, aItem):
        self.__items.append(aItem)

    def getCost(self):
        mySum = 0
        for myCost in self.__items:
            mySum = mySum + myCost.price()
        return mySum

    def showItems(self):
        for myItem in self.__items:
            print(
                "Item : %s , Packing : %s , Price : %5.2f" % (myItem.myName(), myItem.packing().pack(), myItem.price()))


# 设计一个MealBuilder类，负责创建Meal对象
class MealBuilder:
    def prepareVegmeal(self):
        meal = Meal()
        meal.addItem(VegBurger())
        meal.addItem(Coke())
        return meal

    def prepareNonVegMeal(self):
        meal = Meal()
        meal.addItem(ChickenBurger())

        meal.addItem(Pepsi())
        return meal


# 输出
if __name__ == '__main__':
    mealBuilder = MealBuilder()

    vegMeal = mealBuilder.prepareVegmeal()
    print("Veg Meal")
    vegMeal.showItems()
    print("Total Cost : %5.2f" % vegMeal.getCost())

    nonVegMeal = mealBuilder.prepareNonVegMeal()
    print("\n\nNon-Veg Meal")
    nonVegMeal.showItems()
    print("Total Cost : %5.2f" % (nonVegMeal.getCost()))
