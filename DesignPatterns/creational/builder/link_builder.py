# -*- coding:utf-8 -*-


"""
这是一个往 pizza 中添加配料的过程，即 刚开始创建了一个原味的 pizza，随后通过 PizzaBuilder 一步步往 pizza 中添加配料，最终得到一个完整的 pizza。
同时这里实现了一个链式调用，所谓的链式调用，也并不是什么神奇的事情，只是在建造者类的每一个方法在为该对象添加了属性之后返回其本身 —— return self。
"""


class Pizza:
    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = ('Garlic: {}'.format(garlic), 'Extra cheese: {}'.format(cheese))
        return '\n'.join(info)

    def get_pizza_string(self):
        return "pizza_string", self.garlic, self.extra_cheese

    @property
    def pizza_string(self):
        return "pizza", self.garlic, self.extra_cheese

    class PizzaBuilder:
        def __init__(self):
            self.garlic = False
            self.extra_cheese = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)


if __name__ == '__main__':
    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
    print(pizza)
    print(pizza.get_pizza_string())
    print(pizza.pizza_string)

