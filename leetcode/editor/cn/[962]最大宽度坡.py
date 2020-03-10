# 给定一个整数数组 A，坡是元组 (i, j)，其中 i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。 
# 
#  找出 A 中的坡的最大宽度，如果不存在，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
#  
# 
#  示例 2： 
# 
#  输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 50000 
#  0 <= A[i] <= 50000 
#  
# 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def maxWidthRamp0(self, A: List[int]) -> int:
    #     if not A or len(A) == 1:
    #         return 0
    #     if sorted(A, reverse=True) == A and len(set(A)) == len(A):
    #         return 0
    #     N = len(A)
    #     res = 0
    #     left = 0
    #     right = N - 1
    #     while left < right:
    #         if A[left] <= A[right]:
    #             res = max(res, right - left)
    #             left += 1
    #         else:
    #             right -= 1
    #
    #     return res if left != N - 1 else 1

    def maxWidthRamp1(self, A: List[int]) -> int:
        N = len(A) - 1
        while N > 0:
            left = 0
            right = N

            while right < N:
                if A[left] <= A[right]:
                    return right - left
                else:
                    left += 1
                    right += 1
            N -= 1

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        stack = []

        for i in range(len(A)):
            if len(stack) == 0 or A[stack[-1]] > A[i]:  # 防止下标越界，不用A[i]>A[i+1}
                stack.append(i)  # stack中存放下标 ，按值升序

        for j in range(len(A) - 1,  - 1, -1):  # 最大堆的左端肯定在单调栈内
            while stack and A[stack[-1]] <= A[j]:
                k = j - stack.pop()  # 对于栈顶元素来说不可能有更大值， 因此pop出
                res = max(res, k)  # 找到每个单调递增堆中元素的最大宽度坡，max即为整个数组最终结果
        return res

    # sorted根据值排序，顺序求index最大差
    def maxWidthRamp2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        li = sorted(range(n), key=lambda i: A[i])
        last = n
        mx = 0
        for i in li:
            if i < last:
                last = i
            else:
                mx = max(mx, i - last)
        return mx

    # 超时
    # def maxWidthRamp2(self, A: List[int]) -> int:
    #     N = len(A)
    #     left = 0
    #     right = N - 1
    #     res = 0
    #     while left < N:
    #         right = N - 1  # 每次重新置于尾部
    #         while right > 0:
    #             if A[left] <= A[right]:
    #                 res = max(res, right - left)
    #             right -= 1
    #         left += 1
    #     return res
    #
    #     # for i in range(len(A)):
    #     #     for j in range(len(A) - 1, -1, -1):
    #     #         if A[i] <= A[j]:
    #     #             res = max(res, j-i)


# leetcode submit region end(Prohibit modification and deletion)
A = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
B = [2, 3, 4, 1]
print(Solution().maxWidthRamp(A))
