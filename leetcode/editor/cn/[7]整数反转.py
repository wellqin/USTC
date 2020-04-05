# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: 321
#  
# 
#  示例 2: 
# 
#  输入: -123
# 输出: -321
#  
# 
#  示例 3: 
# 
#  输入: 120
# 输出: 21
#  
# 
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        if x is None:
            return
        if x == 0 or all(x == 0 for x in str(x)):
            return 0

        x = str(x).strip()

        flag = True
        if x[0] == "-":
            flag = False
            x = x[1:]

        x = x[::-1].lstrip("0")

        if -2 ** 31 < int(x) < (2 ** 31) - 1:
            return int(x) if flag else -int(x)
        else:
            return 0

    # 效率高
    def reverse0(self, x: int) -> int:
        flag = True if x > 0 else False
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
        res = res if flag else -res
        return res if -2147483648 <= res <= 2147483648 else 0

    def reverse1(self, x: int) -> int:
        # x绝对值转换为字符串 + 字符串逆序 + 转换整数 + 判断正负 + 确认范围
        # 虽然简写但效率不行
        res = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

    def reverse2(self, x: int) -> int:

        flag = 1 if x >= 0 else -1  # 用flag记录整数正负

        new_x = 0
        abs_x = abs(x)

        while abs_x:
            new_x = new_x * 10 + abs_x % 10
            abs_x //= 10  # 注意这里用的是取整除//而非/，不然就返回的是12.3（比如输入是123），正确返回结果应该是12
        new_x = flag * new_x
        return new_x if 2147483648 >= new_x >= -2147483648 else 0


# leetcode submit region end(Prohibit modification and deletion)
x = 1534236469

print(Solution().reverse0(x))
