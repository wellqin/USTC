# 给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。 
# 
#  
# 示例:
# 输入: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# 输出: 3
# 解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
#  
# 
#  注意: 
# 
#  
#  所有在words和 S 里的单词都只由小写字母组成。 
#  S 的长度在 [1, 50000]。 
#  words 的长度在 [1, 5000]。 
#  words[i]的长度在[1, 50]。 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if not S or not words:
            return 0
        N = len(S)
        res = 0
        for word in words:
            # 判断子序列
            ans = self.subarr(word, S)
            res += 1 if ans else 0

        return res

    def subarr(self, word, S):
        if not word:
            return True
        for i in word:
            res = S.find(i)
            if res == -1:
                return False
            else:
                S = S[res + 1:]
        return True

    def numMatchingSubseq1(self, S: str, words: List[str]) -> int:
        # defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(
                iter(w[1:]))  # 存储以w[0]开头的前缀，此时waiting = {'a': [[], ['c', 'd'], ['c', 'e']], 'b': [['b']]}
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)  # 在本题的例子中 it 分别为[]、['c', 'd']、['c', 'e']
        return len(waiting[None])

    def numMatchingSubseq2(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)  # iter() 函数用来生成迭代器
            # 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值  >>>ord('a') = 97
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(Solution().numMatchingSubseq2(S, words))
