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

浅拷贝：内层数据没有拷贝出来，依然指向该位置
深拷贝：完全拷贝出来，二者独立
"""
import copy


a = {"lishuntao": {"company": "hut"},
     "lishuntao1": {"company": "hut1"}
     }

# clear方法
# a.clear()
# print(a)  # {}

# copy,返回浅拷贝
new_dict = a.copy()
new_dict["lishuntao"]["company"] = "HUT"  # new_dict拷贝出"lishuntao"与"lishuntao1"这是浅拷贝，
# 第二层的dict也就是数据结构没有被拷贝出来，因此值会变动。
print(new_dict)  # {'lishuntao': {'company': 'HUT'}, 'lishuntao1': {'company': 'hut1'}}
print(a)  # {'lishuntao': {'company': 'HUT'}, 'lishuntao1': {'company': 'hut1'}}


# 深拷贝
a = {"lishuntao": {"company": "hut"},
     "lishuntao1": {"company": "hut1"}
     }
new_dict = copy.deepcopy(a)
new_dict["lishuntao"]["company"] = "HUT"
print(a)  # {'lishuntao': {'company': 'hut'}, 'lishuntao1': {'company': 'hut1'}}
print(new_dict)  # {'lishuntao': {'company': 'HUT'}, 'lishuntao1': {'company': 'hut1'}}

# fromkeys 将可迭代的对象转换为dict
new_list = ["li", "li1", "li2"]
new_dict = dict.fromkeys(new_list, {"company": "hut"})
# 返回一个新的字典，该字典具有可迭代的键，并且值等于value
print(new_dict)  # {'li': {'company': 'hut'}, 'li1': {'company': 'hut'}, 'li2': {'company': 'hut'}}

# get # 如果没有这个键不会抛异常
value = a.get("lishuntao111", {})
print(value)  # {}

# items()
for key, value in a.items():
    print(key, value)  # lishuntao {'company': 'hut'},lishuntao1 {'company': 'hut1'}

# setdefault
# dict.setdefault(key, default=None)
# setdefault()函数首先和get()方法类似会获取key对应Value, 其次如果键不存在于字典中，将会添加键并将值设为默认值。
new_dict = a.setdefault("litao", "hugongda")
print(new_dict)  # hugongda
print(a)  # {'lishuntao': {'company': 'hut'}, 'lishuntao1': {'company': 'hut1'}, 'litao': 'hugongda'}

# update # 可迭代的对象
# a.update([("lishun","tao"),("li110","hu")])
a.update(lishun='tao', li110="hu")  # 一样的效果
print(a)  # {'lishuntao1': {'company': 'hut1'}, 'lishun': 'tao', 'lishuntao': {'company': 'hut'}, 'li110': 'hu',
# 'litao': 'hugongda'}

