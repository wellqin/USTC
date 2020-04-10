# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        二分查找
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""
"""
public static int binary(int[] arr, int data) {
        int min = 0;
        int max = arr.length - 1;
        int mid;
        while (min <= max) {
            // 无符号位运算符的优先级较低，先括起来
            mid =  min + ((max - min) >>> 1);
            if (arr[mid] > data) {
                max = mid - 1;
            } else if (arr[mid] < data) {
                min = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
"""


class solution:

    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            # 无符号位运算符的优先级较低，先括起来
            # 在 min 和 max 很大的时候，会出现溢出的情况，从而导致数组访问出错。改进一般的做法是这样的：将加法变成减法。
            mid = left + ((right - left) >> 1)
            # mid = left + ((right - left) // 2) //地板除，下取整3//2=1，  而3/2=1.5

            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1
lst = [1,2,3,4,5,6,7,8,9, 10]
print(solution().binarySearch(lst,5))

