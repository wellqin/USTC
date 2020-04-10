# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/8/11
Change Activity:  2019/8/11
-------------------------------------------------
"""
from operator import itemgetter


ages=[1,3,4,7,5,6,2,7,8,8,6]
n=11


def allsum(ages,n):
    res=[0 for i in range(n)]
    index = sorted(range(len(ages)), key=lambda k: ages[k])
    # print(index)
    for i in range(n):
        more=index[i]
        if(index[i]-1>=0and ages[index[i]-1]!=ages[index[i]]):
            more =index[i]-1
        if(index[i]+1<n and ages[index[i]+1]!=ages[index[i]]):
            if(res[more]<res[index[i]+1]):
                more = index[i]+1
        res[index[i]] = res[more] + 100
        # if ages[index[i]]>ages[more]:
        #     res[index[i]] = res[more]+100
        # elif res[more]>0:
        #     res[index[i]]=res[more]
        # else:
        #     res[index[i]]=100

    print(res)
    return sum(res)
print(allsum(ages,n))



# print([index for index, value in sorted(enumerate(ages), key=itemgetter(1))])
#
#
# import numpy as np
#
# print(np.argsort(ages))



ages1=[1,3,4,7,5,6,2,7,8,8,6]
n=11
def allsum1(ages,n):
    if not ages:
        return 0
    if len(ages) == 1:
        return 100
    if len(set(ages)) == 1:
        return 100 * len(ages)

    res = [1 for i in range(n)]
    for i in range(1, len(ages)):
        if ages[i] > ages[i-1]:
            res[i] = res[i-1] + 1

    for i in range(len(ages) - 2, -1, -1):
        # print(ages[i], end=" ")
        if ages[i] > ages[i+1] and res[i] <= res[i+1]:
            res[i] = res[i+1] + 1
    print(res)

    return sum(res) * 100

print(allsum1(ages1,n))














