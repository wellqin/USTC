# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1: 
#
# 
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 
#
# 示例 2: 
#
# 
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 
#
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。 
#

class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        if len(set(nums)) == 1: return len(nums)

        dp = [1 for _ in range(len(nums))]
        dp_num = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[j] + 1 == dp[i]:
                        dp_num[i] += dp_num[j]
        count = 0
        for k in dp:
            if k == max(dp):
                count += 1

        return count

    def find_number_of_LIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        # 记录以第i个元素结尾的LIS
        dp = [1] * n
        # 记录以第i个元素结尾LIS的种类
        dp_num = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:  # 如果j位的数值比i位小，则可加入i位的LIS比较队列
                    if dp[j] + 1 > dp[i]:  # 如果j位前的LIS加上i位数字后的长度比目前所有i位的LIS都长
                        dp[i] = dp[j] + 1  # 把j位的LIS+1赋给i
                        dp_num[i] = dp_num[j]  # 继承j位的LIS种类

                    elif dp[j] + 1 == dp[i]:  # 如果j位前的LIS加上i位数字后的长度和目前i位的LIS相等，说明发现了新的组合
                        dp_num[i] += dp_num[j]  # 把j位的种类数目加给i位
        ans = 0
        lis = max(dp)
        for i in range(n):
            if dp[i] == lis:
                ans += dp_num[i]
        return ans
        # return sum(c for i, c in enumerate(dp_num) if dp[i] == max(dp))


print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]))
print(Solution().find_number_of_LIS([1, 3, 5, 4, 7]))
