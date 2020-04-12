# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.DictFunctions
Description :   
Author :          wellqin
date:             2020/4/12
Change Activity:  2020/4/12
-------------------------------------------------

1.2、dict的常用方法

Dict源码方法：
print(dict.__dict__)

"""


a = {"lishuntao": {"company": "hut"},
     "lishuntao1": {"company": "hut1"}
     }
# clear方法
a.clear()
print(a)  # {}

# copy,返回浅拷贝
# new_dict = a.copy()
# new_dict["lishuntao"]["company"] = "HUT"  #new_dict拷贝出"lishuntao"与"lishuntao1"这是浅拷贝，
# # 第二层的dict也就是数据结构没有被拷贝出来，因此值会变动。
# print(new_dict) #{'lishuntao': {'company': 'HUT'}, 'lishuntao1': {'company': 'hut1'}}
# print(a) #{'lishuntao': {'company': 'HUT'}, 'lishuntao1': {'company': 'hut1'}}

# # 深拷贝
# import copy
#
# new_dict = copy.deepcopy(a)
# new_dict["lishuntao"]["company"] = "HUT"
# print(a)  # {'lishuntao': {'company': 'hut'}, 'lishuntao1': {'company': 'hut1'}}
# print(new_dict)  # {'lishuntao': {'company': 'HUT'}, 'lishuntao1': {'company': 'hut1'}}
#
# # fromkeys 将可迭代的对象转换为dict
# new_list = ["li", "li1", "li2"]
# new_dict = dict.fromkeys(new_list, {"company": "hut"})
# print(new_dict)  # {'li': {'company': 'hut'}, 'li1': {'company': 'hut'}, 'li2': {'company': 'hut'}}
#
# # get #如果没有这个键不会抛异常
# value = a.get("lishuntao111", {})
# print(value)  # {}
#
# # items()
# for key, value in a.items():
#     print(key, value)  # lishuntao {'company': 'hut'},lishuntao1 {'company': 'hut1'}
#
# # setdefault
# new_dict = a.setdefault("litao", "hugongda")
# print(new_dict)  # hugongda
# print(a)  # {'lishuntao': {'company': 'hut'}, 'lishuntao1': {'company': 'hut1'}, 'litao': 'hugongda'}
#
# # update #可迭代的对象
# # a.update([("lishun","tao"),("li110","hu")])
# a.update(lishun='tao', li110="hu")  # 一样的效果
