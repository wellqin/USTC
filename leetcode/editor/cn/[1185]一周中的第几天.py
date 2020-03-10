# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。 
# 
#  输入为三个整数：day、month 和 year，分别表示日、月、年。 
# 
#  您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "F
# riday", "Saturday"}。 
# 
#  
# 
#  示例 1： 
# 
#  输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
#  
# 
#  示例 2： 
# 
#  输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
#  
# 
#  示例 3： 
# 
#  输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给出的日期一定是在 1971 到 2100 年之间的有效日期。 
#  
#  Related Topics 数组
import datetime

"""
平年有28天，闰年有29天。
公元年数可被4整除为闰年,但是整百（个位和十位均为0）的年数必须是可以被400整除的才是闰年(比如1900年不是闰年)
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        w = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            d[1] = 29
        l = [0] * (2100 - 1971 + 1)

        for i in range(1971, 2100):  # 判断区间内每年多少天
            if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
                l[i - 1971] = 366
            else:
                l[i - 1971] = 365

        return w[(sum(l[:year - 1971]) + sum(d[:month - 1]) + day + 4) % 7]

# leetcode submit region end(Prohibit modification and deletion)
day = 18
month = 7
year = 1999
print(Solution().dayOfTheWeek(day, month, year))