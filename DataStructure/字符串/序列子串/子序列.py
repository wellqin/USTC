# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        子序列
Description :   
Author :          wellqin
date:             2020/3/21
Change Activity:  2020/3/21

“子序列”并不要求是连续子序列，只要保证元素前后顺序一致即可，
例如：序列 [4, 6, 5] 是 [1, 2, 4, 3, 7, 6, 5] 的一个子序列；

入门：输出一个序列的所有子序列: 实在太多了 -----> 相当于求子集 2 ** n 种结果
     每一位都有存在不存在两种可能，那么总共是2的n次幂种可能，遍历每一种可能去除存在的数组的元素即为该种情况的子集

300. 最长上升子序列 Medium  （不连续）
     拓展：牛牛数列 + 最长非严格上升子序列

674. 最长连续递增序列 Easy  : 给定一个未经排序的整数数组，找到最长且连续的的递增序列,输出长度  （连续）

673. 最长递增子序列的个数 Medium

128. 最长连续序列 Hard
        # 示例:
        #
        # 输入: [100, 4, 200, 1, 3, 2]
        # 输出: 4
        # 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。 【递增加1】

1143. 最长公共子序列[***] Medium

[491] 递增子序列:找出所有的递增子序列，不是最长的那一个

[152] 乘积最大子序列
        # 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
        # 示例 1:
        # 输入: [2,3,-2,4]
        # 输出: 6
        # 解释: 子数组 [2,3] 有最大乘积 6。

[801] 使序列递增的最小交换次数: pass


-------------------------------------------------
"""
import bisect
from typing import List


class Subsequence:
    # 输出一个序列的所有子序列: 实在太多了 -----> 相当于求子集 2 ** n 种结果
    # 回归实现
    def findAllSubsequence(self, nums):
        res = [[]]
        for num in nums:
            # 新的num元素，依次加到res的每个元素中
            res.extend([subset + [num] for subset in res])
            print(res)
        print(len(res))
        return res

    # 二进制法
    def findAllSubsequence1(self, nums):
        res = []
        end = 2 ** len(nums)  # end = 2**size
        for index in range(end):  # shift index
            li = []
            for j in range(len(nums)):
                # 00,01,10,11 is symmetrical
                if (index >> j) % 2:  # this result is 1, so do not have to write ==
                    li.append(nums[j])
            res.append(li)
        print(len(res))
        return res

    # --------------------------------------------------------------------------------
    # [392]判断子序列
    # 1.挨个比对
    def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            return False
        if s == t:
            return True
        s = list(s)
        t = list(t)
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        res = 0
        while i < m and j < n:
            if s[i] == t[j]:
                res += 1
                i += 1
            j += 1
        return res == m

    # 2.LCS思想：只要s是t的最长公共子序列，那么就是结果了
    def isSubsequence1(self, s: str, t: str) -> bool:
        # 判断s是否为t的子序列
        if not s:
            return True
        if not t:
            return False
        if s == t:
            return True
        # dp创建是如果s, t位置调换则出错
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1] == len(s)

    # 3.利用find函数取巧
    def isSubsequence2(self, s, t):
        #  s 是否为 t 的子序列。
        if not s:
            return True
        for i in s:
            res = t.find(i)
            if res == -1:
                return False
            else:
                t = t[res + 1:]
        return True

    # --------------------------------------------------------------------------------
    # 300. 最长上升子序列 Medium
    # dp方法
    def lengthOfLISelf(self, nums):  # 最长上升子序列 [10, 9, 2, 5, 3, 7, 101, 18]
        if not nums:
            return 0
        # dp[i] 的值代表 nums 前 i 个数字的最长子序列长度。
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # 举一反三：非严格上升子序列,>= 即可
                    dp[i] = max(dp[j] + 1, dp[i])
                    print(dp)
        print(dp)
        return max(dp)  # [1, 1, 1, 2, 2, 3, 4, 4]

    # 二分查找
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            p = bisect.bisect_left(res, nums[i])
            if p == len(res):
                res.append(nums[i])
            else:
                res[p] = nums[i]
            print(res)
        return len(res)

    # --------------------------------------------------------------------------------
    def niuniu(self, A):
        A = [7, 2, 3, 1, 5, 6]
        left = [1 for i in range(len(A))]
        right = [1 for i in range(len(A))]

        ans = 1
        # left是以每个元素作为结尾的最长连续递增子序列的长度
        for i in range(1, len(A)):  # [1, 1, 2, 1, 2, 3]
            if A[i] - A[i - 1] > 0:
                left[i] = left[i - 1] + 1

        # right逆着以每个元素作为开头的连续最长递增子序列的长度值
        for i in range(len(A) - 2, -1, -1):  # [1, 2, 1, 3, 2, 1]
            if A[i] < A[i + 1]:
                right[i] = right[i + 1] + 1

        # 遍历所有除去头尾的点，进行拼接
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i + 1]:
                sum = left[i - 1] + right[i + 1]
                if sum > ans:
                    ans = sum
        return ans + 1

    # --------------------------------------------------------------------------------
    # 674. 最长连续递增序列 Easy  输出长度为
    # 注意：序列要求连续，可理解为子串（上升子串）
    def findLengthOfLCISS(self, nums):
        if not nums:
            return 0
        if len(set(nums)) == 1:
            return 1

        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        print(dp)  # [10, 9, 2, 3, 7, 101, 18] --dp-->[1, 1, 1, 2, 3, 4, 1]
        return max(dp)

    # --------------------------------------------------------------------------------
    # 673. 最长递增子序列的个数 Medium
    def findNumberOfLIS(self, nums):
        nums = [1, 3, 5, 4, 7, 1, -4, -3, -2, -1]

        if not nums:
            return 0
        if len(set(nums)) == 1:
            return len(nums)

        dp = [1 for _ in range(len(nums))]  # 以x结尾的最长子序列个数
        dp_num = [1 for _ in range(len(nums))]  # 以x结尾的最长子序列长度
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 这个长度的递增子序列第一次出现
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dp_num[i] = dp_num[j]

                    elif dp[j] + 1 == dp[i]:  # 发现了新的组合
                        dp_num[i] += dp_num[j]
                    print(dp, dp_num)

        # 注意怎么找出个数
        # nums = [1, 3, 5, 4, 7, 1, -4, -3, -2, -1]
        # [1, 2, 3, 3, 4, 1, 1, 2, 3, 4]
        # [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
        # 个数为3
        return sum(c for i, c in enumerate(dp_num) if dp[i] == max(dp))

    # --------------------------------------------------------------------------------
    # [491]递增子序列: 找出所有的递增子序列，不是最长的那一个
    # 回溯法
    def findSubsequences_hs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []  # 一组解
        incsq = [0]  # 一个解（n元0-1数组）

        def backtrack(t):
            if t == n:
                return
            incsq.append(0)
            s = {}
            for i in range(t + 1, n):  # 遍历第 t + 1~n-1 列（即n个状态)
                if nums[i] >= nums[t] and nums[i] not in s:  # 同一层循环不能有重复数
                    s[nums[i]] = 1
                    incsq[-1] = nums[i]
                    res.append(incsq[:])  # 保存（一个解），注意incsq[:]
                    backtrack(i)
            incsq.pop()  # 回溯，出栈

        # 第一个数单独遍历，避免加入单个数
        s = {}
        for i in range(n):
            if nums[i] not in s:
                s[nums[i]] = 1
                incsq[0] = nums[i]
                backtrack(i)
        return res

    def findSubsequences_dfs(self, nums):
        res = set()
        n = len(nums)

        def helper(loc, tmp):
            if len(tmp) > 1 and tmp not in res:
                res.add(tmp)
            for i in range(loc + 1, n):
                if tmp[-1] <= nums[i]:
                    helper(i, tmp + (nums[i],))

        for i in range(n):
            helper(i, (nums[i],))
        return [list(i) for i in res]

    # --------------------------------------------------------------------------------
    # 最长数值连续序列 Hard
    def longestConsecutive(self, nums):
        nums = [10, 9, 4, 2, 3, 4, 7, 101, 18]
        nums = set(nums)  # 去重
        res = 0
        for x in nums:
            if x - 1 not in nums:  # 找到起点小的
                y = x + 1
                while y in nums:  # 依次向下拓展找下一个
                    y += 1
                res = max(res, y - x)
        return res

    def longestConsecutive1(self, nums):
        nums = [10, 9, 4, 2, 3, 4, 7, 101, 18]
        lookup = dict()

        length = 0
        for num in nums:
            if num not in lookup:  # 若数已在哈希表中：跳过不做处理，若是新数加入：
                left = lookup.get(num - 1, 0)
                right = lookup.get(num + 1, 0)

                cur_length = 1 + left + right
                if cur_length > length:
                    length = cur_length

                lookup[num] = cur_length
                lookup[num - left] = cur_length
                lookup[num + right] = cur_length
        print(lookup)

        return length

    # --------------------------------------------------------------------------------
    # 1143. 最长公共子序列[***] Medium
    def longestCommonSubsequence(self, text1, text2):
        if not text1 or not text2:
            return 0
        # base case
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


nums = [10, 9, 2, 3, 7, 101, 18]
print(Subsequence().longestConsecutive1(nums))
