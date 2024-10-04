# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。 
#
# 示例: 
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

# 利用并查集思想和字典解决，尤其是Python的简洁表述，代码如下：
#

"""
关键是时间复杂度的限制，显而易见的O(nlogn)时间复杂度算法：对数组进行全排序，
然后再扫描一遍排序数组，不过不用试也知道肯定这道题过不了

题目需要在非排序状态下完成连续序列的计算，基本就是在线算法（一般理解是O(n)时间复杂度，来一个处理一个，就像在线更新一般），
使用恰当的数据结构保存重要信息，并在处理新元素时更新。这里需要用字典或并查集数据结构保存已经得到的重要信息，
最根本的信息就是所有已知连续序列的头，尾，和序列长度，那么注意在新处理一个元素时，需要更新这三个重要信息，
最后，遍历所有连续序列的长度，即可得到正确结果

"""


class Solution:
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if nums is None or len(nums) == 0:
    #         return 0
    #
    #     rmap, vmap = {}, {}  # 这里可以使用单一字典形成 key->(rank,value) 映射，然而如此代码比较乱，读者可以一试
    #
    #     for e in nums:
    #         if e not in rmap:
    #             rmap[e], vmap[e] = e, 1  # 新元素初始指向自己，连续序列值value为1
    #             if e + 1 in rmap:  # 若当前元素紧邻右边有元素，当前元素value+=右边元素value
    #                 vmap[e] += vmap[e + 1]
    #             if e - 1 in rmap:  # 若当前元素紧邻左边有元素，更新左边元素的序列头，当前元素指向序列头
    #                 vmap[rmap[e - 1]] += vmap[e]
    #                 rmap[e] = rmap[e - 1]
    #             rmap[rmap[e] + vmap[rmap[e]] - 1] = rmap[e]  # 最后更新当前序列尾的rank，使其指向序列头
    #
    #     tmp, res = max(vmap.items(), key=lambda x: x[1])
    #     return res

    def longestConsecutive(self, nums):
        nums = set(nums)  # 去重
        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res

    def longestConsecutive1(self, nums):
        hash_dict = dict()

        max_length = 0
        for num in nums:
            if num not in hash_dict:  # 若数已在哈希表中：跳过不做处理，若是新数加入：
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
        print(hash_dict)

        return max_length


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive1(nums))
