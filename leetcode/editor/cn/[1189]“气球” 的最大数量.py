# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。 
# 
#  字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：text = "nlaebolko"
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：text = "loonbalxballpoon"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：text = "leetcode"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 10^4 
#  text 全部由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text:
            return 0
        strList = "balloon"
        lookup = {}
        count = 0
        for i in text:
            lookup[i] = lookup.get(i, 0) + 1
        while True:
            for i in strList:
                if i in lookup.keys():
                    lookup[i] -= 1
            if all(i in lookup.keys() and lookup[i] >= 0 for i in strList):
                count += 1
            else:
                break
        return count

    def maxNumberOfBalloons0(self, text: str) -> int:
        if not text:
            return 0
        count = 0
        text_count = collections.Counter(text)
        balloon_count = collections.Counter("balloon")
        while True:
            text_count.subtract(balloon_count)
            if all(text_count[i] >= 0 for i in balloon_count.keys()):
                count += 1
            else:
                break
        return count

    def maxNumberOfBalloons1(self, text: str) -> int:
        """
        取巧做法：
        统计text中b,a,l,o,n的次数，其中l,o两个算一次，因为一个balloon单词里l,o各两个，
        然后取短板，即次数最小值就是结果。
        """
        return min(text.count('b'), text.count('a'), text.count('l') // 2,
                   text.count('o') // 2, text.count('n'))


# leetcode submit region end(Prohibit modification and deletion)
text = "leetcode"
print(Solution().maxNumberOfBalloons(text))
