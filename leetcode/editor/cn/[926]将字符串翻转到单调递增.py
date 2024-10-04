# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调
# 递增的。 
# 
#  我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。 
# 
#  返回使 S 单调递增的最小翻转次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入："00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
#  
# 
#  示例 2： 
# 
#  输入："010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
#  
# 
#  示例 3： 
# 
#  输入："00011000"
# 输出：2
# 解释：我们翻转得到 00000000。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 20000 
#  S 中只包含字符 '0' 和 '1' 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 遍历字符串，找到一个分界点，使得该分界点之前1的个数和分界点之后0的个数之和最小，把分界点之前的1变成0，之后的0变成1
class Solution(object):
    def minFlipsMonoIncr1(self, S):
        """
        :type S: str
        :rtype: int
        """
        m = S.count('0')  # 分界点为0之前，统计之后的0
        res = [m]
        for x in S:
            if x == '1':  # 如果是1，分界点之前1的个数+1，分界点之后0的个数不变
                m += 1
            else:  # 如果是0，分界点之前1的个数不变，分界点之后0的个数减1
                m -= 1
            res.append(m)
        return min(res)

    def minFlipsMonoIncr(self, S: str) -> int:
        # 基本思路是遍历所有分隔点找最小值 s = "00110"
        l, r, _sum = [0], [0], 0
        for i in S:
            if i == '1':
                _sum += 1
            l.append(_sum)  # 将左边全翻转为0需要的翻转次数

        _sum = 0
        for i in reversed(S):
            if i == '0':
                _sum += 1
            r.append(_sum)  # 将右边全翻转为1需要的翻转次数
        r.reverse()
        print([l[i] + r[i] for i in range(len(l))])
        # [3, 2, 1, 2, 3, 2]
        return min(l[i] + r[i] for i in range(len(l)))

    def minFlipsMonoIncr2(self, S: str) -> int:
        zero = one = 0
        res = 0
        for s in S:
            if s == "0":
                zero += 1
            else:
                one += 1
            if zero > one:
                res += one
                zero = 0
                one = 0
        res += zero
        return res

    def minFlipsMonoIncr3(self, S: str) -> int:
        dp = [0 for _ in range(len(S))]

        dp[0] = 1 if S[0] == '1' else 0
        for i in range(1, len(S)):
            dp[i] = dp[i - 1] + 1 if S[i] == '1' else dp[i - 1]

        n = len(S)
        ans = min(dp[n - 1], n - dp[n - 1])
        for i in range(n - 1):
            ans = min(ans, dp[i] + ((n - i - 1) - (dp[n - 1] - dp[i])))
        return ans



# leetcode submit region end(Prohibit modification and deletion)
s = "00110"
print(Solution().minFlipsMonoIncr3(s))