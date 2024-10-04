# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1: 
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2: 
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明： 
#
# 
# num1 和 num2 的长度小于110。 
# num1 和 num2 只包含数字 0-9。 
# num1 和 num2 均不以零开头，除非是数字 0 本身。 
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。 
# 
#

"""

直接一位一位的搞，最后转string, 但是考虑到这样kennel最后str2int(num1) * str2int(num2)
是一个极大的数字可能会导致溢出，所以有了后面的思路2
"""


class Solution(object):
    def multiply(self, num1, num2):
        def str2int(num):
            res = 0
            for i in range(len(num) - 1, -1, -1):
                res += int(num[i]) * pow(10, len(num) - 1 - i)
            return res

        return str(str2int(num1) * str2int(num2))


"""
思路 2 - 时间复杂度: O(N)- 空间复杂度: O(1)******

参考了别人的思路：
m位的数字乘以n位的数字的结果最大为m+n位：
99999 < 1000100 = 100000，最多为3+2 = 5位数。
先将字符串逆序便于从最低位开始计算。
"""


class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lookup = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9}  # 节省查找时间，避免无休止使用ord函数来得到数字
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]

        tmp_res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp_res[i + j] += lookup[num1[i]] * lookup[num2[j]]

        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1) + len(num2)):
            res[i] = tmp_res[i] % 10
            if i < len(num1) + len(num2) - 1:
                tmp_res[i + 1] += tmp_res[i] / 10
        return ''.join(str(i) for i in res[::-1]).lstrip('0')  # 去掉最终结果头部可能存在的‘0’


class Solution2:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0 for _ in range(len(num1 + num2))]  # m位的数字乘以n位的数字的结果最大为m+n位
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j + 1] += int(num1[i]) * int(num2[j])
        carry = 0
        # python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
        # divmod(7, 2) = (3, 1)
        for i in range(len(num1 + num2) - 1, -1, -1):
            carry, res[i] = divmod(res[i] + carry, 10)
        while res[0] == 0:
            res.pop(0)
        return ''.join(map(str, res))


num1 = "123"
num2 = "456"
print(Solution2().multiply(num1, num2))
