#将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。 
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下： 
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。 
#
# 请你实现这个将字符串进行指定行数变换的函数： 
#
# string convert(string s, int numRows); 
#
# 示例 1: 
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
#输出: "LCIRETOESIIGEDHN"
# 
#
# 示例 2: 
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
#输出: "LDREOEIIECIHNTSG"
#解释:
#
#L     D     R
#E   O E   I I
#E C   I H   N
#T     S     G 
# Related Topics 字符串

"""

解题思路：
题目理解：
字符串 s 是以 ZZ 字形为顺序存储的字符串，目标是按行打印。
设 numRows 行字符串分别为 s_1s
1
​
  , s_2s
2
​
  ,..., s_ns
n
​
 ，则容易发现：按顺序遍历字符串 s 时，每个字符 c 在 ZZ 字形中对应的 行索引 先从 s_1s
1
​
  增大至 s_ns
n
​
 ，再从 s_ns
n
​
  减小至 s_1s
1
​
  …… 如此反复。
因此，解决方案为：模拟这个行索引的变化，在遍历 s 中把每个字符填到正确的行 res[i] 。
算法流程： 按顺序遍历字符串 s；
res[i] += c： 把每个字符 c 填入对应行 s_is
i
​
 ；
i += flag： 更新当前字符 c 对应的行索引；
flag = - flag： 在达到 ZZ 字形转折点时，执行反向。
复杂度分析：
时间复杂度 O(N)O(N) ：遍历一遍字符串 s；
空间复杂度 O(N)O(N) ：各行字符串共占用 O(N)O(N) 额外空间。

"""

from typing import *
#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        
#leetcode submit region end(Prohibit modification and deletion)
