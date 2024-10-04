"""
-------------------------------------------------
File Name:        dict
Author :          wellqin
date:             2020/4/30
-------------------------------------------------
"""
"""
注：字典类型是Python中最常用的数据类型之一，它是一个键值对的集合，字典通过键来索引，关联到相对的值，理论上它的查询复杂度是 O(1) 

1)、哈希表 (hash tables)

    1. 哈希表（也叫散列表），根据关键值对(Key-value)而直接进行访问的数据结构。
    2. 它通过把key和value映射到表中一个位置来访问记录，这种查询速度非常快，更新也快。
    3. 而这个映射函数叫做哈希函数，存放值的数组叫做哈希表。 
    4. 通过把每个对象的关键字k作为自变量，通过一个哈希函数h(k)，将k映射到下标h(k)处，并将此对象存储在这个位置。

2)、具体操作过程

    1. 数据添加：把key通过哈希函数转换成一个整型数字，然后就将该数字对数组长度进行取余，取余结果就当作数组的下标，将value存储在以该数字为下标的数组空间里。
    2. 数据查询：再次使用哈希函数将key转换为对应的数组下标，并定位到数组的位置获取value。
    3、{“name”:”zhangsan”,”age”:26} 字典如何存储的呢? 
        1. 比如字典{“name”:”zhangsan”,”age”:26}，那么他们的字典key为name、age，假如哈希函数h(“name”) = 1、h(“age”)=3,
        2. 那么对应字典的key就会存储在列表对应下标的位置，[None, “zhangsan”, None, 26 ]
    4、解决hash冲突:拉链法（append链表尾部） + 开放寻址法
        开放寻址法中，所有的元素都存放在散列表里，当产生哈希冲突时，通过一个探测函数计算出下一个候选位置，
        如果下一个获选位置还是有冲突，那么不断通过探测函数往下找，直到找个一个空槽来存放待插入元素。
"""


class MyDict(object):
    """
    dict() -> new empty dictionary

    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs

    dict(iterable) -> new dictionary initialized as if via:

    print(dict([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]))  # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2}
    print(dict([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]))  # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2}

        d = {}
        for k, v in iterable:
            d[k] = v

    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def clear(self):  # real signature unknown; restored from __doc__
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def copy(self):  # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D """
        pass

    @staticmethod  # known case
    def fromkeys(*args, **kwargs):  # real signature unknown
        """ Returns a new dict with keys from iterable and values equal to value. """
        pass

    def get(self, k, d=None):  # real signature unknown; restored from __doc__
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def items(self):  # real signature unknown; restored from __doc__
        """ D.items() -> a set-like object providing a view on D's items """
        pass

    def keys(self):  # real signature unknown; restored from __doc__
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

    def pop(self, k, d=None):  # real signature unknown; restored from __doc__
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        pass

    def popitem(self):  # real signature unknown; restored from __doc__
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.
        """
        pass

    def setdefault(self, k, d=None):  # real signature unknown; restored from __doc__
        """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
        pass

    def update(self, E=None, **F):  # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

    def values(self):  # real signature unknown; restored from __doc__
        """ D.values() -> an object providing a view on D's values """
        pass

    def __contains__(self, *args, **kwargs):  # real signature unknown
        """ True if D has a key k, else False. """
        pass

    def __delitem__(self, *args, **kwargs):  # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y):  # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, seq=None, **kwargs):  # known special case of dict.__init__
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, value) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs):  # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self):  # real signature unknown; restored from __doc__
        """ D.__sizeof__() -> size of D in memory, in bytes """
        pass

    __hash__ = None
