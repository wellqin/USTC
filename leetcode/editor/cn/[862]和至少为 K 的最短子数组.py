#返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。 
#
# 如果没有和至少为 K 的非空子数组，返回 -1 。 
#
# 
#
# 
# 
#
# 示例 1： 
#
# 输入：A = [1], K = 1
#输出：1
# 
#
# 示例 2： 
#
# 输入：A = [1,2], K = 4
#输出：-1
# 
#
# 示例 3： 
#
# 输入：A = [2,-1,2], K = 3
#输出：3
# 
#
# 
#
# 提示： 
#
# 
# 1 <= A.length <= 50000 
# -10 ^ 5 <= A[i] <= 10 ^ 5 
# 1 <= K <= 10 ^ 9 
# 
#

"""
解题方案
思路
1 - 时间复杂度: O(N) - 空间复杂度: O(N) ** ** **

首先想到用前缀和数组，对于每一个prefix[i]，找到一个最大的j使得j < i
并且prefix[i] - prefix[j] >= K， 那么i - j就是一个符合题目条件的长度，取所有这样的长度中的最小值即可，如果没有就返回 - 1

但是这样也是O(N ^ 2)
的一个解法，无疑是不行的

优化一下，维护一个deque
opt，使得opt(y) = largest
x
with prefix[x] <= prefix[y] - K

我们发现两个规律：


If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if P[x1] <= P[y] - K, then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller. This implies that our candidates x for opt(y) will have increasing values of P[x].

If opt(y1) = x, then we do not need to consider this x again. For if we find some y2 > y1 with opt(y2) = x, then it represents an answer of y2 - x which is worse (larger) than y1 - x.

beats 90.53%

deque 是一个双端队列, 如果要经常从两端append 的数据, 选择这个数据结构就比较好了, 如果要实现随机访问,不建议用这个,请用列表.
deque 优势就是可以从两边append ,appendleft 数据. 这一点list 是没有的.
"""
import collections, sys, heapq


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = [0] + A
        prefix = [0] * len(A)
        for i in range(1, len(A)):
            prefix[i] = prefix[i - 1] + A[i]

        # # 记录和，dp[i] = sum(A[:i])
        # dp = [0] * (len(A) + 1)
        # for i in range(1, len(dp)):
        #     dp[i] = dp[i - 1] + A[i - 1]



        opt = collections.deque()  # opt(y) = largest x with prefix[x] <= prefix[y] - K
        res = sys.maxsize

        for x2, px2 in enumerate(prefix):

            # 规律1: If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1
            while opt and px2 <= prefix[opt[-1]]:
                opt.pop()

            # 规律2: If opt(y1) = x, then we do not need to consider this x again.
            while opt and px2 - prefix[opt[0]] >= K:
                res = min(res, x2 - opt.popleft())

            opt.append(x2)

        return res if res != sys.maxsize else -1


    def shortestSubarray1(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heap, res, sm = [], sys.maxsize, 0
        heapq.heappush(heap, (0, -1))
        for i, num in enumerate(A):
            sm += num
            diff = sm - K
            while heap and (heap[0][0] <= diff or i - heap[0][1] >= res):
                preSum, preIndex = heapq.heappop(heap)
                if i - preIndex < res:
                    res = i - preIndex
            heapq.heappush(heap, (sm, i))
        return res if res != sys.maxsize else -1


#cA = [2,-1,2]
A =  [4,-1,2,3]
# K = 3
K = 5

print(Solution().shortestSubarray(A, K))
print(Solution().shortestSubarray1(A, K))




"""
思路
2 - 时间复杂度: O(N) - 空间复杂度: O(N) ** ** **

同样的原理，我们可以用heapq来实现，参考cnkyzz

We
cannot
use
this
tuple
later as length
will
always
increase as i
increases !
For
the
current
tuple, it
might
be
the
new
shortest
subarray if i - preIndex < l and we
update
res
beats
15.26 %
"""