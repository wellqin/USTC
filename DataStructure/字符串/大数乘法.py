# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        数学
Description :   
Author :          wellqin
date:             2019/8/2
Change Activity:  2019/8/2
-------------------------------------------------
"""
"""
我们学了那么多年的数学，做了那么多年的乘法，却不曾仔细总结其中的规律，至少是没有用这种程序化的逻辑概括过。
这个计算过程想想也是很有意思，还是总结下。

以15*15=225为例：
个位数是5*5=25，留5，进位2.
十位数稍微复杂点，有两个乘法都是以他为底，并且他还可能从个位得到进位，还需要进位给百位。
百位至少在本例简单点，1*1是不用再进位了，但是也需要从十位得到一次进位。

 
所以15*15=225的乘法流程总结起来就是，从输出结果的角度，以每个位（k）去找对应的以他为底的乘法计算，

直观的说：
k=0时（个位），5*5=25，进位2，留5；
k=1时（十位），前者的10乘以后者的5，后者的10乘以前者的5，他们是共享底位（十位）的。50+50=100，算上25进的那个20，结果就是120,120的1进给百位；
k=2，百位的10*10=100，加上进位的100，就是200。每个位都得到了结果，最后225。

其实总的来看，有点像二项式展开的意思。核心思想：你可以给每位一次性计算出所有以它为最低位的乘法结果并累加，确定了本位的数值，
然后进位，算其他位。（额外的，再考虑进位问题）


时间关系，不做图啰嗦了，在纸上写一下基本的乘法计算过程，很容易看出来，其他注释写到代码中：
（num1: str, num2: str) -> str:
"""
# #给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':  # 有0就不用乘了。
            return '0'
        res = ''
        carry = 0  # 初始化
        # 两个数的长度，分别都减1
        m = len(num1) - 1
        n = len(num2) - 1
        # m和n都是len减1，是因为，15*15中，不算被动进位，能用来主动计算乘法的，最高位就是百位，10*10=100，是主动计算的最高位。
        # k就在[0,m+n]的区间：代表主动计算乘法的位（最后多出来的进位单独给出）。k=0，i和j都是0,5*5，对应个位结果。
        # k=1，i和j分别是0、1和1、0组合，是10和5或者5和10，对应十位的结果，
        # k=2，i和j分别是1、1（其他组合不满足筛选条件，我计算的就是百位，不能把5也拿来用吧，把乘法写一下就出来了），代表10和10相乘，对应百位结果。
        # m位的数字乘以n位的数字的结果最大为m+n位

        for k in range(m + n + 1):
            print('k:', k)
            # i是所有输出位，包括k=m+n，不包括m+n+1，其实就是遍历所有可能的num1和num2的单独一位，做一个总的累加
            # i、j他俩是严格针对k的互补关系。i = 时，j = 1；i = 1时，j = 0，他们都对应结果的“下标”k=1，也就是“十位”
            sum = carry  # 先把进位计算进来（这个顺序其实无所谓，但是如果不是先进位，就要给sum清零了）
            for i in range(k + 1):  # k其实就是结果位。i和j是根据k做的互补，严格对应一个结果底位。
                j = k - i
                if i <= m and j <= n:
                    index_i = m - i  # 转换，字符串形式，i=0其实代表的是最大的那个数，不是最小的，index_i才是最小的数。
                    index_j = n - j
                    sum += int(num1[index_i]) * int(num2[index_j])

            # 拼接结果字符串，遍历完当前k对应的所有i和j的组合，当前位的结果已经出炉，可以拼接了。比如15*15的最后一位5*5，是由当前位停留结果5和进位2组成的，当前结果就留在这。
            res = str(sum % 10) + res  # 从低位向高位迭代，使用新的sum模，后加res的拼接方式。
            carry = sum // 10  # 进位，5*5=25，进位2

        if carry:  # 最后一位了，k迭代的是乘法计算，当然可能发生进位，比如33*44中，k是0到2，最高位3*4肯定要进位的
            res = str(carry) + res
        return res

    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        觉得这样写才是最容易理解的，看一个具体的🌰:
        input: num1, num2 = '91', '91'
        tmp_res = [1,18,81,0]
        res = [1,8,2,8]
        最终返回 "8281"
        要注意最终返回头部可能会有‘0’，所以我们用lstrip去除一下

        1. 把数据放到列表中，即list1和list2。
        2. 每个list1列表中的第i个元素，与list2列表中的第j个元素相乘，把对应乘积的结果放到下标为（i+j）的列表中。
        3. 如果该位的结果大于10，则向后进1。
        """

        lookup = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9}  # 节省查找时间，避免无休止使用ord函数来得到数字
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]  # 先将字符串逆序便于从最低位开始计算。

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

    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        position = len(res) - 1

        for n1 in reversed(num1):
            pos = position
            for n2 in reversed(num2):
                res[pos] += int(n1) * int(n2)
                res[pos - 1] += res[pos] // 10
                res[pos] %= 10
                pos -= 1
            position -= 1

        pointer = 0
        while pointer < len(res) - 1 and res[pointer] == 0:
            pointer += 1

        return ''.join(map(str, res[pointer:]))

num1 = '123'
num2 = '456'
ss = Solution()
res = ss.multiply(num1, num2)
res1 = ss.multiply1(num1, num2)
res2 = ss.multiply2(num1, num2)
print(res)
print(res1)
print(res2)

