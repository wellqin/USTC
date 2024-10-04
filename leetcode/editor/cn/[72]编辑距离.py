# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作： 
#
# 
# 插入一个字符 
# 删除一个字符 
# 替换一个字符 
# 
#
# 示例 1: 
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
#
# 示例 2: 
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# Related Topics 字符串 动态规划

"""


问题1：如果 word1[0..i-1] 到 word2[0..j-1] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要几步呢？
答： 先使用 k 步，把 word1[0..i-1] 变换到 word2[0..j-1]，消耗 k 步。再把 word1[i] 改成 word2[j]，就行了。
    如果 word1[i] == word2[j]，什么也不用做，一共消耗 k 步，否则需要修改，一共消耗 k + 1 步。

问题2：如果 word1[0..i-1] 到 word2[0..j] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要消耗几步呢？
答： 先经过 k 步，把 word1[0..i-1] 变换到 word2[0..j]，消耗掉 k 步，再把 word1[i] 删除，这样，word1[0..i] 就完全变成了 word2[0..j]了。
    一共 k + 1 步。

问题3：如果 word1[0..i] 到 word2[0..j-1] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要消耗几步呢？
答： 先经过 k 步，把 word1[0..i] 变换成 word2[0..j-1]，消耗掉 k 步，接下来，再插入一个字符 word2[j],
    word1[0..i] 就完全变成了 word2[0..j] 了。

从上面三个问题来看，word1[0..i] 变换成 word2[0..j] 主要有三种手段，用哪个消耗少，就用哪个
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        正常写法，O(n^2)存储
        """
        '''
                动态规划 
                step1: 状态  
                首先只定义一维 DP[i] 不能有效简化问题的处理
                使用 二维 DP[i][j]，表示 word1 的 i 个字母 与 word2 的 第 j 个字母 相同 需要的操作步骤数
                将最对 word1 处理 转化为 对 word1 和 word2 均处理
                word1 插入一个字符   DP[i-1][j] + 1 ->  DP[i][j]
                word1 删除一个字符 = word2 插入一个字符  DP[i][j-1] + 1 -> DP[i][j]
                word1 替换一个字符 = word1 word2 都替换一个字符 DP[i-1][j-1] + 1 -> DP[i][j]
                step2: 动态方程
                DP[i][j]  A、word1 的 i 个字母 与 word2 的 第 j 个字母 相同
                             DP[i][j] =  DP[i-1][j-1]  #不操作
                          B、不相同,需要进行 插入 删除 或者 替换操作
                             DP[i][j]  =  min(DP[i-1][j] + 1,DP[i][j-1] + 1,DP[i-1][j-1]+1)

        '''
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = 0
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for j in range(1, n2 + 1):
            dp[0][j] = j
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[n1][n2]

    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        优化存储，O(n)（两行dp）
        """
        n1, n2 = len(word1), len(word2)
        dp1 = [0] * (n2 + 1)  # 保留两行
        dp2 = [0] * (n2 + 1)
        dp1[0] = 0
        for j in range(1, n2 + 1):
            dp1[j] = j
        for i in range(1, n1 + 1):
            dp2[0] = i
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp2[j] = dp1[j - 1]
                else:
                    dp2[j] = min(dp1[j], dp2[j - 1], dp1[j - 1]) + 1
            dp1, dp2 = dp2, dp1
        return dp1[n2]

    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        优化存储，O(n)（一行dp）
        """
        n1, n2 = len(word1), len(word2)
        dp = [0] * (n2 + 1)  # 保留一行
        dp[0] = 0
        for j in range(1, n2 + 1):
            dp[j] = j
        for i in range(1, n1 + 1):
            old_dp_j = dp[0]
            dp[0] = i
            for j in range(1, n2 + 1):
                old_dp_j_1, old_dp_j = old_dp_j, dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = old_dp_j_1
                else:
                    dp[j] = min(dp[j], dp[j - 1], old_dp_j_1) + 1
        return dp[n2]
