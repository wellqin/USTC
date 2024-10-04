# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        水仙花数
Description :   
Author :          wellqin
date:             2019/9/23
Change Activity:  2019/9/23
-------------------------------------------------
"""
n = int(input())
for num in range(10**(n-1), 10**n):
    if sum(map(lambda i: int(i)**n, str(num))) == num:  # map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
                           # 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
        print(list(map(lambda i: int(i)**n, str(num))))  # [1, 125, 27]  -->>  [1, 5, 3]  -->>  153
        print(num)
        break



"""
#include <stdio.h>
int main()
{
    int hun, ten, ind, n;
    printf("result is:");
    for( n=100; n<1000; n++ )  /*整数的取值范围*/
    {
        hun = n / 100;
        ten = (n-hun*100) / 10;
        ind = n % 10;
        if(n == hun*hun*hun + ten*ten*ten + ind*ind*ind)  /*各位上的立方和是否与原数n相等*/
            printf("%d  ", n);
    }
    printf("\n");
   
    return 0;
}
"""
print(153/100)   # 1.53
print(153//100)  # 1
