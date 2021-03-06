# 一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。 
# 
#  给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以
# 假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。 
# 
#  如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。
# 
# 
#  请注意： 
# 
#  
#  石子的数量 ≥ 2 且 < 1100； 
#  每一个石子的位置序号都是一个非负整数，且其 < 231； 
#  第一个石子的位置永远是0。 
#  
# 
#  示例 1: 
# 
#  
# [0,1,3,5,6,8,12,17]
# 
# 总共有8个石子。
# 第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
# 第三个石子在序号为3的单元格的位置， 以此定义整个数组...
# 最后一个石子处于序号为17的单元格的位置。
# 
# 返回 true。即青蛙可以成功过河，按照如下方案跳跃： 
# 跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着 
# 跳2个单位到第4块石子, 然后跳3个单位到第6块石子, 
# 跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。
#  
# 
#  示例 2: 
# 
#  
# [0,1,2,3,4,8,9,11]
# 
# 返回 false。青蛙没有办法过河。 
# 这是因为第5和第6个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        大致思路：
        保存相邻石子间的距离为一个列表，方便判断
        维护一个每个位置跳跃步长列表的字典
        :param stones:
        :return:
        """
        if stones[1] > 1:
            return False
        # 相邻石子间隔的距离
        steps = [stones[i]-stones[i-1] for i in range(1, len(stones))]
        # 如果全是1、2，直接返回true
        if max(steps) < 3:
            return True
        # 定义一个字典维护每个位置跳跃过的步长的列表
        jump = {0:[1]}
        # i为当前位置
        i = 0
        while i < len(steps):
            # 指向下一个位置
            i += 1
            if not jump.get(i-1):
                # 如果当前位置没有发生跳跃则表示是跳过的石头直接下个位置
                continue
            # 弹出当前位置步长列表，也可以直接get，每次pop出来应该能减小空间占用
            step = jump.pop(i-1)
            # 存放当前位置添加过的步长，防止重复添加
            used_step = set()
            while step:
                # 如果i到了末尾则表示成功过河
                if i == len(steps):
                    return True
                # 每次从步长列表弹出一个步长
                cur_step = step.pop()
                if cur_step in used_step:
                    continue
                # 步长加入集合防止重复
                used_step.add(cur_step)
                # 当前位置能跳哪些步长
                able_step = [cur_step-1,cur_step,cur_step+1]
                for step_ in able_step:
                    start = 0
                    for j in range(i, len(steps)):
                        # 累加跳的步长
                        start += steps[j]
                        # 有匹配的直接添加到字典里匹配位置上的步长列表里
                        if start == step_:
                            jump.setdefault(j,[]).append(step_)
                        # 一旦超出则直接退出循环进入下一个步长匹配
                        if start > step_:
                            break
        # 没有新的位置匹配则表示没能过河
        return False



# leetcode submit region end(Prohibit modification and deletion)
stones = [0, 1, 3, 5, 6, 8, 12, 17]
ss = Solution()
print(ss.canCross(stones))
