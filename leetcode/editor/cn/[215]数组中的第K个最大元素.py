#在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
#
# 示例 1: 
#
# 输入: [3,2,1,5,6,4] 和 k = 2
#输出: 5
# 
#
# 示例 2: 
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
#输出: 4 
#
# 说明: 
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
#
def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


class Solution:
    def findKthLargest(self, nums, k):
        if nums == None:
            return
        if len(nums) == 1:
            return 1

        nums = quick_sort(nums)
        return nums[len(nums) - k]

# 堆思路
class Solution1:
    def findKthLargest(self, nums, k):
        '''
        在未排序的数组中找到第 k 个最大的元素。
        输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
        输出: 4
        '''
        # 维护k长度最小堆
        hp = [-2**30] * k
        for n in nums:
            # n值小于最小堆堆顶, 跳过
            if n < hp[0]:
                continue
            # 最小堆堆化O(n)
            # 替换最小堆堆顶,将堆中的最小值提升到堆顶  其他值已经有序
            pos, smallpos = 0, 1
            while smallpos < k:
                rightpos = smallpos + 1
                if rightpos < k and not hp[smallpos] < hp[rightpos]:
                    smallpos = rightpos
                hp[pos] = hp[smallpos]
                pos = smallpos
                smallpos = 2 * pos + 1

            # 前一步是父子节点之间提升最小值,
            # pos重新赋值后, 以pos为叶子节点到根节点之间的元素进行排序.
            while pos > 0:
                parentpos = (pos - 1) >> 1
                parentval = hp[parentpos]
                # 父节点的值大于子节点时, 父节点的值降低到子节点
                if parentval > n:
                    hp[pos] = parentval
                    pos = parentpos
                    continue
                break
            hp[pos] = n

        return hp[0]
        