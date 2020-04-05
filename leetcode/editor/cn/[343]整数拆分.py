# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 
# 
#  说明: 你可以假设 n 不小于 2 且不大于 58。 
#  Related Topics 数学 动态规划

"""

小学生找规律办法！从n = 2开始，答案为{1, 2, 4, 6, 9, 12, 18, 27, 36, 54}。这其中有什么规律？！

答案是，当n >= 5开始，res[i]为res[i - 1]加上前面最大的偶数的一半。

举例说明，

当n == 5， 答案为4 + （4 / 2）== 6

当 n == 6，答案为6 + ( 6 / 2) == 9

当n == 7，答案为 9 + (6 / 2) == 12 (因为上一个9不是偶数，所以依然取6的一半）

当n == 8，答案为 12 + （12 / 2）== 18

当n == 9， 答案为 18 + （18 / 2） == 27


"""
"""
相对于“自上而下”通过“递归”实现的“记忆化搜索”，“动态规划”则是通过“递推”、“自底向上”的方式求解问题。
因此，“动态规划”的思路是依次求出 dp[0]、dp[1]、dp[2]、……，这是外层循环，最后一个状态就是我们要求的。
而每一个 dp[i] 又和它之前的状态有关，因此还需要一层循环，即内层循环，内层循环的写法就是我们分析出的“状态转移方程”。

dp[i]存储到i时的最大乘积
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n):
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2
        dp = [1] * (n + 1)

        """
        外层循环从 3 开始遍历，一直到 n 停止。内层循环 j 从 1 开始遍历，一直到 i 之前停止，它代表着数字 i 可以拆分成 j + (i - j)。
        但 j * (i - j)不一定是最大乘积，因为i-j不一定大于dp[i - j]（数字i-j拆分成整数之和的最大乘积），
        这里要选择最大的值作为 dp[i] 的结果。
        
        以8为例：3*5 = 15 此时j * (i - j)不一定是最大乘积
                3 * dp[5] = 3*3*2 = 18 为最大乘积
        """

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])

        print(dp)  # [1, 1, 2, 3, 4, 6, 9, 12, 18, 27, 36]
        return dp[-1]

    def integerBreak1(self, n):
        if n == 2:
            return 1
        res = -1
        for i in range(1, n):
            res = max(res, max(i * (n-i), i * self.integerBreak1(n - i)))
        return res

    # 记忆化搜索-自顶向下
    # 记忆化搜索是将目标F(n)不断转化为求F(n-1),F(n - 2),...,F(2),F(1)，过程中将计算过的值存起来
    # 从递归树中看出来这是一个从上到下的过程，一般将之称为"自顶向下"。
    def integerBreak2(self, n):
        memory = [0 for _ in range(n+1)]
        if n == 2:
            return 1
        if memory[n] != 0:  # memory的初始值为0，如果它不为0，说明已经计算过了，直接返回即可
            return memory[n]
        res = -1
        for i in range(1, n):
            res = max(res, max(i * (n-i), i * self.integerBreak1(n - i)))
        memory[n] = res
        return res



        
# leetcode submit region end(Prohibit modification and deletion)
n = 10
print(Solution().integerBreak(n))