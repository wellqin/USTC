#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。 
#
# 注意你不能在买入股票前卖出股票。 
#
# 示例 1: 
#
# 输入: [7,1,5,3,6,4]
#输出: 5
#解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
#
# 示例 2: 
#
# 输入: [7,6,4,3,1]
#输出: 0
#解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
#

class Solution(object):
    # 递归求解，无非就是固定首尾指针，不是首指针往右边移，就是尾指针往左边移。所以写两个递归式即可得出答案。
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 定义获取的最大利润
        max_profit = 0
        if len(prices) <= 1:
            return max_profit

        def back(start, end, max_profit):
            if start >= end:
                return max_profit
            profit = prices[end] - prices[start]
            max_profit = back(start + 1, end, max(max_profit, profit))
            max_profit = back(start, end - 1, max(max_profit, profit))
            return max_profit

        return back(0, len(prices) - 1, 0)

    # 本题采用双指针法，从左至右依次遍历,
    # 递归TLE了，既然递归行不通，那就只能是老老实实的通过遍历数组来找出答案了。
    # 本题其实和接雨水题目很类似
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 定义获取的最大利润
        max_profit = 0
        if len(prices) <= 1:
            return max_profit

        # 分别定义股票的最小价格以及最高价格
        min_price = prices[0]
        max_price = 0
        for index in range(len(prices)):
            if prices[index] <= min_price:
                min_price = prices[index]
            elif prices[index] - min_price > max_price:
                max_price = prices[index] - min_price
        return max_price


    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        动态规划解法
        基本思路：用两个变量，一个存储当前最大的收益，一个存储当前的最小值。用当前的卖出价值，减去前面的最小值，即为当前收益。
        空间复杂度比较好, O(l)，时间复杂度一般，应该是O(n)。一开始是用min函数找前面的最小值，超时了。代码如下：

        """
        if (len(prices)<=1):
            return 0
        min_p=prices[0]
        max_p=0
        for i in range(len(prices)):
            min_p= min(min_p,prices[i])
            # 最大利润=max{前一天最大利润, 今天的价格 - 之前最低价格}
            max_p= max(max_p,prices[i]-min_p)
        return max_p

    # 一遍遍历的方法
    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 2 ** 31
        maxprofit = 0
        plen = len(prices)
        for x in prices:
            if x < minprice:
                minprice = x
            elif x - minprice > maxprofit:
                maxprofit = x - minprice
        return maxprofit

    def maxProfit_git(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        opt = [0] * len(prices)
        for i in range(1, len(prices)):
            opt[i] = max(opt[i - 1] + prices[i] - prices[i - 1], 0)
        return max(opt)

    def maxProfit_git1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        res, max_cur = 0, 0
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur + prices[i] - prices[i - 1])
            res = max(res, max_cur)
        return res

    def maxProfit_git2(self, prices):
        if not prices: return 0
        minprice, maxprofit = float("inf"), 0

        for i in range(len(prices)):
            minprice = min(minprice, prices[i])  # 记录当前最小
            maxprofit = max(maxprofit, prices[i] - minprice)  # 计算 当前最大利润（之前最大利润 与 当前价格与之前最小价格之差 的最大值）
        return maxprofit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))
print(Solution().maxProfit1(prices))
print(Solution().maxProfit_1(prices))
print(Solution().maxProfit_git(prices))
print(Solution().maxProfit_git1(prices))
print(Solution().maxProfit_git2(prices))