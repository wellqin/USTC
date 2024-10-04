#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/9 20:40
@Author  : qinwei05


继承
dataclass装饰器会检查当前class的所有基类，如果发现一个dataclass，就会把它的字段按顺序添加进当前的class，随后再处理当前class的field。
所有生成的方法也将按照这一过程处理，因此如果子类中的field与基类同名，那么子类将会无条件覆盖基类。
子类将会根据所有的field重新生成一个构造函数，并在其中初始化基类。

"""

from dataclasses import dataclass, asdict, astuple, is_dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        """
        total_cost
        @return:
        """
        return self.unit_price * self.quantity_on_hand


# 继承演示
@dataclass
class Base:
    x: float = 25.0
    y: int = 0


@dataclass
class C(Base):
    z: int = 10
    x: int = 15


if __name__ == '__main__':
    inventoryItem = InventoryItem("Book", 10, 10)
    print(inventoryItem.quantity_on_hand)
    print(inventoryItem.total_cost())
    print(asdict(inventoryItem))
    print(astuple(inventoryItem))
    print(is_dataclass(inventoryItem))

    print(C())  # C(x=15, y=0, z=10)

