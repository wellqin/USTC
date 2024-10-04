# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex + 1):
            # 用 1 先填充每行所有元素
            cur = [1] * (i + 1)
            # 由上一行循环生成当前行元素（除两端）
            for j in range(1, i):
                cur[j] = pre[j - 1] + pre[j]
            pre = cur
        return cur


# leetcode submit region end(Prohibit modification and deletion)
