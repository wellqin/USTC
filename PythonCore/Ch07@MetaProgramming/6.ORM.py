# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        6.ORM
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.6、通过元类实现ORM系统
"""

# 需求  实现ORM（Django实现ORM原理）
import numbers


class Field:
    pass


class IntField(Field):
    """
    验证是否满足整数
    #数据描述符
    """
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        # 初级判断
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")

    def __get__(self, instance, owner):  # 调用属性的时候会调用此魔法函数
        return self._value

    def __set__(self, instance, value):  # 给属性赋值的时候会调用此魔法函数 因此应该在这里面判断值是否是整数
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):
    """
    验证是否满足字符串字段
    """

    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        # 初级判断
        if max_length is None:
            raise ValueError("you must spcify max_lenth for charfiled")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):  # 当给属性赋值的时候调用此魔法函数，因此判断逻辑在这里进行
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self._value = value


# 元类中实现将传入的值取出来
# 从BaseModel来到元类之中，实例化ModelMetaClass类对象之前，先执行__new__当中的逻辑，类名为ModelMetaClass，因此进入else
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":  # BaseModel中是没有定义age，name的，需要判断，否则后面直接出错
            return super().__new__(cls, name, bases, attrs, **kwargs)  # 实例化类对象之前，必须返回参数
        # 字段是封装到这个中的
        fields = {}  # 表相关的列
        #       name      bases          attrs 对应下面的type实现类对象的参数（因为继承了type类对象）
        # type("User", (BaseClass, ), {"name":"user", "say":say})  # type也可以实现类对象（传入参数）
        for key, value in attrs.items():
            if isinstance(value, Field):  # 判断字段中的值是否为同一实例化对象，都继承Field，因此为True
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)  # 取出类
        # 表名是封装到这个_meta中的
        _meta = {}
        db_table = name.lower()  # 将模型类（User）变成小写，赋值给表名，此处表示没有db_table = "user"时，默认表名
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)  # 取出类中的属性
            if table is not None:  # 已经显示设置数据库表的表名
                db_table = table
        _meta["db_table"] = db_table
        # 将表名和字段封装给attrs（dict）参数
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        # 删除attrs参数中的Meta，已经把表名取出来了，没有必要存储到attrs参数中
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)  # attrs已经重新组合


# 当实例化User之前，进入到这里，要实例化BaseModel类对象之前，寻找到metaclass进入metaclass逻辑中
class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):  # 从元类返回回来的参数修改过的attrs，进入到这里被初始化
        # kwargs，因为attrs是字典，因此需要遍历这个
        for key, value in kwargs.items():
            setattr(self, key, value)  # 将attrs["_meta"]、与attrs["fields"]初始化成对象属性
        return super().__init__()

    def save(self):  # 拼凑字符串
        fields = []
        values = []
        # {"name":"lishuntao","age":18}
        for key, value in self.fields.items():
            db_column = value.db_column  # 调用对象属性（CharField的对象name，IntField的对象age）
            if db_column is None:  # 如果默认列表名字没有填入
                db_column = key.lower()  # 就使用字段名的小写作为表名
            # 将表名全部加入到fields列表中
            fields.append(db_column)
            # 将属性的值取出来
            value = getattr(self, key)
            values.append(str(value))  # values=",".join(values)时要使用同种类型
        # SQL语句的书写 fields=",".join(fields)这个是将列表变成字符串
        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"],
                                                                   fields=",".join(fields), values=",".join(values))
        pass


# 继承的是元类，当实例化此类对象之前的时候，会去寻找metaclass，如果没有就去父(基)类中寻找metaclass
class User(BaseModel):
    """
    实现表的字段，以及数据类型限制
    CharField和IntField都是属性描述符
    """
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=1, max_value=100)

    class Meta:
        db_table = "user"  # 这里定义的表是什么表，user表。默认用类名User的小写作为表名，在数据库迁移时，会生成user表


if __name__ == "__main__":
    # 实现orm数据的赋值与保存，为了防止属性报错，用了之前的属性描述符
    user = User()
    user.name = "lishuntao"
    user.age = 18
    # user = User(name="lishuntao", age=18)，这样写的话需要User类中进行init，但是写法不是Django风格，所以User类继承BaseModel
    # 在BaseModel中完成相关__init__工作
    user.save()
