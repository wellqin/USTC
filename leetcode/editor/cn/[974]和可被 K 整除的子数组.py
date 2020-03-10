# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。 
# 
#  
# 
#  示例： 
# 
#  输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 30000 
#  -10000 <= A[i] <= 10000 
#  2 <= K <= 10000 
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        N = len(A)
        nums = [[] for _ in range(len(A))]
        # nums表示所有连续子数组的和（包含单个元素）
        for i in range(N):
            res = 0
            for j in range(i, N):
                res += A[j]
                nums[i].append(res)
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # print(nums[i][j])
                if nums[i][j] % k == 0:
                    count += 1
        return count

    def subarraysDivByK1(self, A: List[int], K: int) -> int:
        N = len(A)
        count = 0
        # nums表示所有连续子数组的和（包含单个元素）
        for i in range(N):
            res = 0
            for j in range(i, N):
                res += A[j]
                if res % k == 0:
                    count += 1
        return count

    def subarraysDivByK2(self, A: List[int], K: int) -> int:
        pre_sum, result = 0, 0
        dic = {0: 1}  # initial
        # 第一个mod为0,不需要跟别人配对儿，自己就能成为一个结果，为了统一后面的流程，提前+1了

        for val in A:
            pre_sum = (pre_sum + val) % K  # 累加並對 K取餘
            print(pre_sum)
            if pre_sum in dic:  # 判斷是否在字典內，即有(同餘的值)
                result += dic[pre_sum]  # 更新結果
            # key不存在 則默認val=0 + 1 、key在 則 val +=1
            # ~>若再下次出現"同餘"時，"同餘"出現3次，會有兩種可能性
            # ~>若再下次出現"同餘"時，"同餘"出現4次，會有三種可能性...
            dic[pre_sum] = dic.get(pre_sum, 0) + 1

        return result

    def subarraysDivByK3(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for _ in range(len(A) + 1)]  # s代表前缀和，即s[i]表示sum(A[:i])
        kcnt = [0 for _ in range(K)]  # kcnt[i]代表s中有多少个元素 mod K 为i
        for i in range(len(A)):
            s[i + 1] = s[i] + A[i]
        for item in s:
            kcnt[item % K] += 1
        print(s, kcnt)

        return sum(x * (x - 1) // 2 for x in kcnt)

    def subarraysDivByK4(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        size = len(A)
        s = [0] * (size + 1)
        for i in range(size):  # s为前缀和
            s[i + 1] = s[i] + A[i]

        kcnt = map(lambda x: x % K, s)
        cnt = Counter(kcnt)

        ret = 0
        for key, val in cnt.items():
            if val > 1:
                ret += val * (val - 1) // 2
        return ret


# leetcode submit region end(Prohibit modification and deletion)

A = [4, 5, 0, -2, -3, 1]
k = 5
print(Solution().subarraysDivByK(A, k))
print(Solution().subarraysDivByK1(A, k))
print(Solution().subarraysDivByK2(A, k))
print(Solution().subarraysDivByK3(A, k))
print(Solution().subarraysDivByK4(A, k))

AA = [
    [4, 9, 9, 7, 4, 5],
    [5, 5, 3, 0, 1],
    [0, -2, -5, -4],
    [-2, -5, -4],
    [-3, -2],
    [1]
]
