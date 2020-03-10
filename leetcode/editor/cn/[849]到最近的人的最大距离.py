# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。 
# 
#  至少有一个空座位，且至少有一人坐在座位上。 
# 
#  亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。 
# 
#  返回他到离他最近的人的最大距离。 
# 
#  示例 1： 
# 
#  输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。 
#  
# 
#  示例 2： 
# 
#  输入：[1,0,0,0]
# 输出：3
# 解释： 
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。
#  
# 
#  提示： 
# 
#  
#  1 <= seats.length <= 20000 
#  seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxDistToClosestSelf(self, seats: List[int]) -> int:
        # Default
        if not seats:
            return 0
        res = 0
        dis = 0
        tmp = [i for i in range(len(seats)) if seats[i] == 1]

        if len(tmp) == 1:
            if abs(tmp[0]) > abs(len(seats) - tmp[0]):
                return tmp[0]
            else:
                return len(seats) - 1
        else:
            for i in range(1, len(tmp)):
                res = max(res, tmp[i] - tmp[i - 1])
                dis = max(dis, tmp[i] + res // 2)
            return dis

    def maxDistToClosest(self, seats):
        length = len(seats)
        # 把有人坐的座位下标提出来
        tmp = [i for i in range(len(seats)) if seats[i] == 1]

        # 考虑最左最右是零的情况
        ans = max(tmp[0], length - tmp[-1] - 1)
        # 离他最近的人的最大距离即相邻有人坐的座位之间距离的一半
        for i in range(1, len(tmp)):
            if (tmp[i] - tmp[i-1]) // 2 > ans:
                ans = (tmp[i] - tmp[i-1]) // 2
        return ans

    def maxDistToClosest3(self, seats):
        # 开头/结尾为0, 则特殊处理
        tmp = [i for i in range(len(seats)) if seats[i] == 1]
        max_count = max(tmp[0], len(seats) - tmp[-1] - 1)

        # 找到0的最大个数
        count, start, end = 0, None, None
        for i in range(len(seats)):
            if seats[i] == 0 and start is None:
                start = i
            if seats[i] == 1 and start is not None and end is None:
                end = i
            if start is not None and end is not None:
                count = max(count, end - start)
                start, end = None, None
        if count % 2 == 0:
            return max(max_count, count // 2)
        return max(max_count, count // 2 + 1)




# leetcode submit region end(Prohibit modification and deletion)
A = [1, 0, 0, 0, 1, 0, 1]
B = [0, 0, 1, 0, 0, 1, 0]
print(Solution().maxDistToClosest3(B))
