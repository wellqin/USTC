#给定两个二进制字符串，返回他们的和（用二进制表示）。 
#
# 输入为非空字符串且只包含数字 1 和 0。 
#
# 示例 1: 
#
# 输入: a = "11", b = "1"
#输出: "100" 
#
# 示例 2: 
#
# 输入: a = "1010", b = "1011"
#输出: "10101" 
# Related Topics 数学 字符串
"""

a or b 为空，最简单
唯一的问题是如果有进位的处理，
进位的处理就是先让其中的一个数和‘1’做addBinary处理 ，然后再用addBinary


抖个机灵*

先把 a,b用bin(数，原本的进制)转为二进制
得到a+b的二进制数
将二进制数转为字符串
截取字符串的索引为2的元素到最后（前两位为0b所以要截取）
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        ans=bin(a+b)
        ans=str(ans)
        ans=ans[2:]
        return ans
"""


#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '' or b == '':
            return a + b
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(b[:-1], self.addBinary(a[:-1], '1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
        
#leetcode submit region end(Prohibit modification and deletion)
a = "111"
b = "101"
print(Solution().addBinary(a, b))