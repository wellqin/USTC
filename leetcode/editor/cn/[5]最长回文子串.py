# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1： 
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
#
# 示例 2： 
#
# 输入: "cbbd"
# 输出: "bb"
# 
#

"""
方法一：暴力匹配 （Brute Force）
暴力解法虽然时间复杂度高，但是思路清晰、编写简单，因为编写的正确性高，完全可以使用暴力匹配算法检验我们编写的算法的正确性。

"""


class Solution0:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        answer = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j + 1]
                print(temp)
                if temp == temp[::-1] and len(temp) > maxlen:
                    maxlen = len(temp)
                    answer = temp
        return answer


s = "babad"
print("answer is :", Solution0().longestPalindrome(s))


"""
方法二：中心扩散法
中心扩散法的想法很简单：遍历每一个索引，以这个索引为中心，利用“回文串”中心对称的特点，往两边扩散，看最多能扩散多远。
要注意一个细节：回文串的长度可能是奇数，也可能是偶数。

"""


class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size == 0:
            return ''

        # 至少是 1
        maxlen = 1
        ans = s[0]

        for i in range(size):
            odd, odd_len = self.__center_spread(s, size, i, i)
            even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = odd if odd_len >= even_len else even
            if len(cur_max_sub) > maxlen:
                maxlen = len(cur_max_sub)
                ans = cur_max_sub

        return ans

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数

        1、如果传入重合的索引编码，进行中心扩散，此时得到的最长回文子串的长度是奇数；
        2、如果传入相邻的索引编码，进行中心扩散，此时得到的最长回文子串的长度是偶数。

        """
        l = left
        r = right

        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1


s = "babad"
print(Solution().longestPalindrome(s))


"""
如果一个字符串的左右边界相等，以下二者之一成立即可：
1、去掉左右边界以后的字符串不构成区间，即“ s[l + 1, r - 1] 至少包含两个元素”的反面，即 l - r >= -2，或者 r - l <= 2；
2、去掉左右边界以后的字符串是回文串，具体说，它的回文性决定了原字符串的回文性。

于是整理成“状态转移方程”：
dp[l, r] = (s[l] == s[r] and (r - l <= 2 or dp[l + 1, r - 1]))
or 是短路运算，因此，如果收缩以后不构成区间，那么就没有必要看继续 dp[l + 1, r - 1] 的取值。

"""


class Solution1:
    # 可读性不好
    def longestPalindrome1(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        # dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        # “状态”定义为原字符串的一个子串是否为回文子串
        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True  # 单个字符一定是回文串，因此把对角线先初始化为 True

        for r in range(1, size):  # 只有 1 个字符的情况在最开始做了判断，左边界一定要比右边界小，因此右边界从 1 开始
            for l in range(r):
                if s[l] == s[r]:
                    # 在 s[i] == s[j] 成立和 j - i < 3 的前提下，直接可以下结论，dp[i][j] = true，否则才执行状态转移
                    if r - l < 3:  # j - i <= 2
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]
                else:
                    dp[l][r] = False

                if dp[l][r]:
                    cur_len = r - l + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = l
        return s[start:start + max_len]


# s = "abc1234321ab"
# print(Solution().longestPalindrome(s))


def manacher(s):
    s = '#' + '#'.join(s) + '#'  # step1

    RL = [0] * len(s)  # 各种初始化一下，RL是回文半径数组
    mx = 0
    id = 0
    Maxlen = 0

    for i in range(len(s)):
        if i < mx:  # i在maxright左边
            RL[i] = min(RL[2 * id - i], mx - i)
        else:  # i在maxright右边，以i为中心的回文串还没扫到，此时，以i为中心向两边扩展
            RL[i] = 1  # RL=1：只有自己

        # 以i为中心扩展，直到左！=右or达到边界(先判断边界)
        while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] += 1

        # 更新Maxright pos:
        if RL[i] + i - 1 > mx:
            mx = RL[i] + i - 1
            id = i

        # 更新最长回文子串的长;
        Maxlen = max(Maxlen, RL[i])
    s = s[RL.index(Maxlen) - (Maxlen - 1):RL.index(Maxlen) + (Maxlen - 1)]
    s = s.replace('#', '')
    return s

# print(manacher('abc1234321ab'))
