#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。 
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
#与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
#


# 固定一个元素
#
# 用两个指针来循环

"""
排序+双指针
算法流程：
1.特判，对于数组长度n，如果数组为Null或者数组长度小于3，返回[]。
2.对数组进行排序，并定义res，保存最接近和。
3.遍历排序后数组：
    对于重复元素，跳过，避免重复计算（也可以不跳过）
    令左指针L=i+1,右指针R=n-1,当L<R时，执行循环：
        *令cur_sum = nums[i]+nums[L]+nums[R,如果cur_sum=targe,返回target
        *若abs(cur_sum-target)<abs(res-target),说明cur_sum更接近目标，更新res
        *若cur_sum-target大于0，说明nums[R]太大，R左移
        *若cur_sum-target小于0，说明nums[L]太小，L右移
复杂度分析 O(n**2)|O(1)

"""
from typing import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if(not nums or n<3):
            return None
        nums.sort()
        res=float("inf")  # 最接近和
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                cur_sum=nums[i]+nums[L]+nums[R]
                if(cur_sum==target):
                    return target
                if(abs(cur_sum-target)<abs(res-target)):
                    res=cur_sum
                if(cur_sum < target):
                    L+=1
                else:
                    R-=1
        return res






        