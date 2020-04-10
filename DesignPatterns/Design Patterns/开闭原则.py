# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        开闭原则
Description :   
Author :          wellqin
date:             2020/4/5
Change Activity:  2020/4/5
-------------------------------------------------
"""

"""
开闭原则

开闭原则就是说对扩展开放，对修改关闭。在程序需要进行拓展的时候，不能去修改原有的代码，实现一个热插拔的效果。
所以一句话概括就是：为了使程序的扩展性好，易于维护和升级。想要达到这样的效果，我们需要使用接口和抽象类

以书店销售书籍为例。原来书店只按照原价销售小说，现在由于经济下滑，书店为了生存开始打折销售：所有50元以上的书8折销售，其他书籍9折销售。
"""


class Book(object):
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    def get_name(self):
        pass

    def get_price(self):
        pass

    def get_author(self):
        pass

    def get_book_info(self):
        pass


class NovelBook(Book):
    def __init__(self, name, price, author):
        super().__init__(name, price, author)

    def get_name(self):
        return self.name

    def get_price(self):  # 打折处理不应该直接修改这里的get_price
        return self.price

    def get_author(self):
        return self.author

    def get_book_info(self):
        return "Book name: " + self.get_name() + "  Book author: " + self.get_author() + "  Book price: " + str(
            self.get_price() / 100.0) + "元"


# 需求变化后需要提供打折处理，根据开闭原则，增加一个子类OffNovelBook类覆写get_price()，而不是直接在原NovelBook类上做修改。
class OffNovelBook(NovelBook):  # 新增子类用于扩展
    def __init__(self, name, price, author):
        super().__init__(name, price, author)

    # def get_name(self):
    #     return self.name

    def get_price(self):
        origin_price = super(OffNovelBook, self).get_price()
        off_price = 0
        if origin_price >= 5000:
            off_price = origin_price * 0.8
        else:
            off_price = origin_price * 0.9

        return off_price

    # def get_author(self):
    #     return self.author

    def get_book_info(self):
        off_book_info = super().get_book_info()
        return off_book_info


# 此处初始化区属于高层次模块因为业务需求变更也需要相应修改，但修改越少越好
class BookStore(object):
    def __init__(self):
        self.book_list = []
        # self.book_list.append(NovelBook("西游记", 3000, "吴承恩"))
        # self.book_list.append(NovelBook("三国演义", 6000, "罗贯中"))
        # self.book_list.append(NovelBook("红楼梦", 8000, "曹雪芹"))

        self.book_list.append(OffNovelBook("西游记", 3000, "吴承恩"))
        self.book_list.append(OffNovelBook("三国演义", 6000, "罗贯中"))
        self.book_list.append(OffNovelBook("红楼梦", 8000, "曹雪芹"))

    def sell(self, book):
        print("Sell Info: {}".format(book.get_book_info()))


if __name__ == '__main__':
    book_store = BookStore()
    for book in book_store.book_list:
        book_store.sell(book)
