# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/12
Change Activity:  2019/7/12
-------------------------------------------------
"""
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# for i in nums[len(nums):0:-1]:
#     print(i)
import sys,bisect
dp = [-4,6, -3,8,-9]

bisect.insort(dp, 1)
print(bisect.insort(dp, 1))
print("dp= ", dp)







res = -sys.maxsize
k =12


sums, cur_sum, cur_max = [sys.maxsize], 0, -sys.maxsize
for sm in dp:
    bisect.insort(sums, cur_sum)
    cur_sum += sm
    ll = bisect.bisect_left(sums, cur_sum - k)
    rr = sums[bisect.bisect_left(sums, cur_sum - k)]
    pp = cur_sum - sums[bisect.bisect_left(sums, cur_sum - k)]
    cur_max = max(cur_max, cur_sum - sums[bisect.bisect_left(sums, cur_sum - k)])
res = max(res, cur_max)


def maxSubArray2(dp):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(dp)
    maxSum = [dp[0] for i in range(n)]
    for i in range(1, n):
        maxSum[i] = max(maxSum[i - 1] + dp[i], dp[i])
    return max(maxSum)
print(maxSubArray2(dp))


