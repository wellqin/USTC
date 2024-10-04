# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        hash
Description :   
Author :          wellqin
date:             2019/9/10
Change Activity:  2019/9/10
-------------------------------------------------
"""
# -*- coding: utf-8 -*-
import hashlib


class ConHash(object):
    def __init__(self, nodes=None, n_number=15):
        """
        :param nodes:           所有的节点
        :param n_number:        一个节点对应多少个虚拟节点
        :return:
        """
        self._n_number = n_number  # 每一个节点对应多少个虚拟节点，这里默认是3个
        self._node_dict = dict()  # 用于将虚拟节点的hash值与node的对应关系
        self._sort_list = []  # 用于存放所有的虚拟节点的hash值，这里需要保持排序
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """
        添加node，首先要根据虚拟节点的数目，创建所有的虚拟节点，并将其与对应的node对应起来
        当然还需要将虚拟节点的hash值放到排序的里面
        这里在添加了节点之后，需要保持虚拟节点hash值的顺序
        :param node:
        :return:
        """
        for i in range(self._n_number):
            node_str = "%s#%s" % (node, i)  # 虚拟节点=n#真实节点#n
            key = self._gen_key(node_str)  # 计算虚拟节点的key
            self._node_dict[key] = node  # key和真实节点的对应关系
            self._sort_list.append(key)
        self._sort_list.sort()

    def remove_node(self, node):
        """
        这里一个节点的退出，需要将这个节点的所有的虚拟节点都删除
        :param node:
        :return:
        """
        for i in range(self._n_number):
            node_str = "%s#%s" % (node, i)
            key = self._gen_key(node_str)
            del self._node_dict[key]
            self._sort_list.remove(key)

    def get_node(self, key_str):
        """
        返回这个字符串应该对应的node，这里先求出字符串的hash值，然后找到第一个小于等于的虚拟节点，然后返回node
        如果hash值大于所有的节点，那么用第一个虚拟节点
        :param :
        :return:
        """
        if self._sort_list:
            key = self._gen_key(key_str)
            for node_key in self._sort_list:
                if key <= node_key:
                    return self._node_dict[node_key]
            return self._node_dict[self._sort_list[0]]
        else:
            return None

    @staticmethod
    def _gen_key(key_str):
        """
        通过key，返回当前key的hash值，这里采用md5
        :param key:
        :return:
        """
        md5_str = hashlib.md5(key_str.encode(encoding='UTF-8')).hexdigest()  # 16进制
        # return long(md5_str, 16)  #p3 不支持long
        # print(int(md5_str,16),md5_str)
        # return int(md5_str,16)
        return md5_str  # 用hexdigest当key也没问题


# ring = ConHash(["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"])
ring = ConHash(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
print(ring.get_node("DV001"))
print(ring.get_node("DV002"))
print(ring.get_node("DV003"))
print(ring.get_node("DV004"))
print(ring.get_node("DV005"))
print(ring.get_node("DV006"))
print(ring.get_node("DV007"))
print(ring.get_node("DV008"))
print(ring.get_node("DV009"))
print(ring.get_node("DV010"))
print(ring.get_node("DV011"))
print(ring.get_node("DV012"))
print(ring.get_node("DV013"))
print(ring.get_node("DV014"))
print(ring.get_node("DV015"))
print(ring.get_node("DV016"))
'''
 测试结果很不均匀。。。。
 (vgflask64) d:\fk\work\python\vgflask64\work\test>python tchash.py
192.168.1.2
192.168.1.2
192.168.1.1
192.168.1.3
192.168.1.2
192.168.1.1
192.168.1.3
192.168.1.1
192.168.1.3
192.168.1.3
192.168.1.1
192.168.1.3
'''
