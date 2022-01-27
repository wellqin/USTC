# -*- coding:utf-8 -*-


from enum import Enum
import random

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    pool = dict()

    def __new__(cls, tree_type, *args, **kwargs):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = super().__new__(cls, *args, **kwargs)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def __init__(self, size):
        self.size = size

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({},{})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1

    for _ in range(3):
        t1 = Tree(TreeType.cherry_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1

    for _ in range(5):
        t1 = Tree(TreeType.peach_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1

    print(Tree.pool)


if __name__ == '__main__':
    main()
