# -*- coding:utf-8 -*-


from enum import Enum
import random

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    """
    一个简单的享元模式：即通过其中的__new__魔法方法来限制类的实例化，只允许实例化不同类型的对象。

    通过一个类型池，若需要实例化的类型在该类型池中，则直接返回该类型池中的对象，由于返回的是同一对象，故其共享不可变的属性（tree_type），
    而在执行完成__new__()方法之后，变化执行__init__魔法方法，则这时候该对象的属性便会发生改变，故不共享可变的属性（size）。
    """
    pool = dict()

    def __new__(cls, tree_type, *args, **kwargs):  # 在__new__方法中实现类不可变数据的共享
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = super(Tree, cls).__new__(cls, *args, **kwargs)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def __init__(self, size):  # 在__init__方法中实现了可变数据的独立，即不共享
        self.size = size

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({},{})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(3):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    print("=" * 30)

    for _ in range(3):
        t1 = Tree(TreeType.cherry_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    print("=" * 30)

    for _ in range(3):
        t1 = Tree(TreeType.peach_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    print("=" * 30)

    print(Tree.pool)
    print(tree_counter)


if __name__ == '__main__':
    main()
