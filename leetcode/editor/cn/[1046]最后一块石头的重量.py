#有一堆石头，每块石头的重量都是正整数。 
#
# 每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下： 
#
# 
# 如果 x == y，那么两块石头都会被完全粉碎； 
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 
# 
#
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。 
#
# 
#
# 提示： 
#
# 
# 1 <= stones.length <= 30 
# 1 <= stones[i] <= 1000 
# 
#
import heapq
from bisect import insort
class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x != y:
                insort(stones, y - x)  # 用于向一个有序的列表插入数据， 插入后自动有序
        if not stones:
            return 0
        return stones[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >=2:                                           #有两个石头就要进行消除,直到最后0或者1
            a = stones.index(max(stones))     #把最大和第二大的取出来,有剩余就放回去,没有剩余就不返还值
            b_max = stones.pop(a)
            a_2 = stones.index(max(stones))
            b_max_2 = stones.pop(a_2)
            if b_max != b_max_2:
                stones.append(b_max-b_max_2)
            print(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0


class Solution2:
    def lastStoneWeight(self, stones):
        import heapq
        heap = []
        for i in stones:
            heapq.heappush(heap, i*-1)
        left_stones = len(stones)
        while left_stones > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, first-second)
                left_stones -= 1
            else:
                left_stones -= 2
        if left_stones == 1:
            return heapq.heappop(heap) * (-1)
        else:
            return 0


print(Solution().lastStoneWeight([10, 11, 12]))
print(Solution().lastStoneWeight([2, 2]))
