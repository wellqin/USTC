#给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。 
#
# 示例: 
#
# 输入: matrix = [[1,0,1],[0,-2,3]], k = 2
#输出: 2 
#解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
# 
#
# 说明： 
#
# 
# 矩阵内的矩形区域面积必须大于 0。 
# 如果行数远大于列数，你将如何解答呢？ 
# 
#
# 思路 1 - 时间复杂度: O(row * col^2)- 空间复杂度: O(row)******
# 最大子矩形的方法是先压维，即将几行压到一行里，然后最大子序列和就可以了（把几行压到一行里的方法是先预处理个前缀和）
import bisect, sys


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        res = -sys.maxsize

        for l in range(col):
            dp = [0] * row
            for r in range(l, col):
                for i in range(row):
                    dp[i] += matrix[i][r]

                # Find the max subarray no more than K
                sums, cur_sum, cur_max = [sys.maxsize], 0, -sys.maxsize
                for sm in dp:
                    bisect.insort(sums, cur_sum)
                    cur_sum += sm
                    cur_max = max(cur_max, cur_sum - sums[bisect.bisect_left(sums, cur_sum - k)])
                res = max(res, cur_max)
                # n = len(dp)
                # maxSum = [dp[0] for i in range(n)]
                # for i in range(1, n):
                #     maxSum[i] = max(maxSum[i - 1] + dp[i], dp[i])
                # return max(maxSum)
        return res

matrix = [[1,0,1],[0,-2,3]]
k = 2
print(Solution().maxSumSubmatrix(matrix, k))
print("==============================================")



dp = [-4,6, -3,8,-9]
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
print(res)


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















