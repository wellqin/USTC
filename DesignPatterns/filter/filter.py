# -*- coding:utf-8 -*-

from abc import abstractmethod, ABCMeta


# 创建一个类，在该类上应用标准
class Person:
    _name = ""
    _gender = ""
    _marital_status = ""

    def __init__(self, in_name, in_gender, in_marital_status):
        self._name = in_name
        self._gender = in_gender
        self._marital_status = in_marital_status

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_marital_status(self):
        return self._marital_status

    @staticmethod
    def print_persons(in_persons):
        for a_person in in_persons:
            print("Person : [ Name : {0}, Gender : {1}, Marital Status : {2}]".format(a_person.get_name(),
                                                                                      a_person.get_gender(),
                                                                                      a_person.get_marital_status()))


# 为标准（Criteria）创建一个接口
class Criteria(metaclass=ABCMeta):
    @abstractmethod
    def meet_criteria(self, in_persons):
        pass


# 创建实现了Criteria接口的实体类
class CriteriaMale(Criteria):
    def meet_criteria(self, in_persons):
        male_persons = []
        for a_person in in_persons:
            if a_person.get_gender().upper() == "MALE":
                male_persons.append(a_person)
        return male_persons


class CriteriaFemale(Criteria):
    def meet_criteria(self, in_persons):
        female_persons = []
        for a_person in in_persons:
            if a_person.get_gender().upper() == "FEMALE":
                female_persons.append(a_person)
        return female_persons


class CriteriaSingle(Criteria):
    def meet_criteria(self, in_persons):
        single_persons = []
        for a_person in in_persons:
            if a_person.get_marital_status().upper() == "SINGLE":
                single_persons.append(a_person)
        return single_persons


class AndCriteria(Criteria):
    _criteria = None
    _otherCriteria = None

    def __init__(self, in_criteria, in_other_criteria):
        self._criteria = in_criteria
        self._otherCriteria = in_other_criteria

    def meet_criteria(self, in_persons):
        # 获得第一次过滤结果
        first_criteria_person = self._criteria.meet_criteria(in_persons)
        # 返回第二次过滤结果
        return self._otherCriteria.meet_criteria(first_criteria_person)


class OrCriteria(Criteria):
    _criteria = None
    _otherCriteria = None

    def __init__(self, in_criteria, in_other_criteria):
        self._criteria = in_criteria
        self._otherCriteria = in_other_criteria

    def meet_criteria(self, in_persons):
        # 先用Criteria分别构造数据
        first_criteria_items = self._criteria.meet_criteria(in_persons)
        other_criteria_items = self._otherCriteria.meet_criteria(in_persons)
        # 完成或运算
        for a_person in other_criteria_items:
            if a_person not in first_criteria_items:
                first_criteria_items.append(a_person)
        return first_criteria_items


# 调用输出
if __name__ == '__main__':
    persons = [
        Person("Robert", "Male", "Single"),
        Person("John", "Male", "Married"),
        Person("Laura", "Female", "Married"),
        Person("Diana", "Female", "Single"),
        Person("Mike", "Male", "Single"),
        Person("Bobby", "Male", "Single")
    ]
    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()
    singleMale = AndCriteria(single, male)
    singleOrFemale = OrCriteria(single, female)

    print("\nMales: ")
    Person.print_persons(male.meet_criteria(persons))
    print("\nFemales: ")
    Person.print_persons(female.meet_criteria(persons))
    print("\nSingle: ")
    Person.print_persons(single.meet_criteria(persons))
    print("\nSingle Males: ")
    Person.print_persons(singleMale.meet_criteria(persons))
    print("\nSingle or Female:")
    Person.print_persons(singleOrFemale.meet_criteria(persons))
