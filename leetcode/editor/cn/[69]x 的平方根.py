# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。 
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
#
# 示例 1: 
#
# 输入: 4
# 输出: 2
# 
#
# 示例 2: 
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
# 
#


class Solution:
    def mySqrt(self, x: int) -> int:
        if not x or x == 0 or x == 1:
            return x
        nums = list(range(x))
        l = 0
        r = x//2
        while l <= r:
            mid = l + ((r - l) >> 1)
            if pow(nums[mid], 2) == x:
                return nums[mid]
            elif pow(nums[mid], 2) < x:
                l = mid + 1
            elif pow(nums[mid], 2) > x:
                r = mid - 1

        return -1

    def mySqrt1(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        l = 1
        r = x // 2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            elif x >= (mid + 1) * (mid + 1):
                l = mid + 1
        return mid


x = 9
print(Solution().mySqrt1(x))
