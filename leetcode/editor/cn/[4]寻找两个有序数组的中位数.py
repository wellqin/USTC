# -*- coding: utf-8 -*-
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
#
# 你可以假设 nums1 和 nums2 不会同时为空。 
#
# 示例 1: 
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 
#
# 示例 2: 
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5

# for循环遍历两个列表失败—— ValueError: too many values to unpack
# nums1, = [3, 4, 6, 7, 8, 11]
# nums2, = [2, 5, 9, 12, 17, 20]
# https://blog.csdn.net/hehedadaq/article/details/81836025

"""
在pyhon3中/是真除法。                   3/2=1.5
如果想在python3使用地板除，是//          3//2=1         7 // 2=3
%表示求余数                            5%2=1

" / "  就表示 浮点数除法，返回浮点结果;
" // "   表示整数除法。
"""

from typing import List


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m = len(nums1)
#         n = len(nums2)
#         # 最后要找到合并以后索引是 median_index 的这个数
#         median_index = (m + n) >> 1
#
#         # nums1 的索引
#         i = 0
#         # nums2 的索引
#         j = 0
#
#         # 计数器从 -1 开始，在循环开始之前加 1
#         # 这样在退出循环的时候，counter 能指向它最后赋值的那个元素
#         counter = -1
#
#         res = [0, 0]
#         while counter < median_index:
#             counter += 1
#             # 先写 i 和 j 遍历完成的情况，否则会出现数组下标越界
#             if i == m:
#                 res[counter & 1] = nums2[j]
#                 j += 1
#             elif j == n:
#                 res[counter & 1] = nums1[i]
#                 i += 1
#             elif nums1[i] < nums2[j]:
#                 res[counter & 1] = nums1[i]
#                 i += 1
#             else:
#                 res[counter & 1] = nums2[j]
#                 j += 1
#             # print(res)
#             # 每一次比较，不论是 nums1 中元素出列，还是 nums2 中元素出列
#             # 都会选定一个数，因此计数器 + 1
#
#         # 如果 m + n 是奇数，median_index 就是我们要找的
#         # 如果 m + n 是偶数，有一点麻烦，要考虑其中有一个用完的情况，其实也就是把上面循环的过程再进行一步
#
#         if (m + n) & 1:
#             return res[counter & 1]
#         else:
#             return sum(res) / 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 为了让搜索范围更小，我们始终让 num1 是那个更短的数组，PPT 第 9 张
        if len(nums1) > len(nums2):
            # 这里使用了 pythonic 的写法，即只有在 Python，中可以这样写
            # 在一般的编程语言中，得使用一个额外变量，通过"循环赋值"的方式完成两个变量的地址的交换
            nums1, nums2 = nums2, nums1

        # 上述交换保证了 m <= n，在更短的区间 [0, m] 中搜索，会更快一些
        m = len(nums1)
        n = len(nums2)

        # 使用二分查找算法在数组 nums1 中搜索一个索引 i，PPT 第 9 张
        left = 0
        right = m

        # 这里使用的是最简单的、"传统"的二分查找法模板
        while left <= right:
            # 尝试要找的索引，在区间里完成二分，为了保证语义，这里就不定义成 mid 了
            # 用加号和右移是安全的做法，即使在溢出的时候都能保证结果正确，但是 Python 中不存在溢出
            # 参考：https://leetcode-cn.com/problems/guess-number-higher-or-lower/solution/shi-fen-hao-yong-de-er-fen-cha-zhao-fa-mo-ban-pyth/
            i = (left + right) >> 1
            j = ((m + n + 1) >> 1) - i

            # 边界值的特殊取法的原因在 PPT 第 10 张
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]

            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # 交叉小于等于关系成立，那么中位数就可以从"边界线"两边的数得到，原因在 PPT 第 2 张、第 3 张
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 已经找到解了，分数组之和是奇数还是偶数得到不同的结果，原因在 PPT 第 2 张
                if (m + n) & 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                # 这个分支缩短边界的原因在 PPT 第 8 张，情况 ②
                right = i - 1
            else:
                # 这个分支缩短边界的原因在 PPT 第 8 张，情况 ①
                left = i + 1
        raise ValueError('传入无效的参数，输入的数组不是有序数组，算法失效')


class Solution1:
    # 这题很自然地想到归并排序，再取中间数，但是是nlogn的复杂度，题目要求logn
    # 所以要用二分法来巧妙地进一步降低时间复杂度
    # 思想就是利用总体中位数的性质和左右中位数之间的关系来把所有的数先分成两堆，然后再在两堆的边界返回答案
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # 让nums2成为更长的那一个数组
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # 如果两个都为空的异常处理
        if n == 0:
            raise ValueError

        # nums1中index在imid左边的都被分到左堆，nums2中jmid左边的都被分到左堆
        imin, imax = 0, m

        # 二分答案
        while imin <= imax:
            imid = imin + (imax - imin) // 2
            # 左堆最大的只有可能是nums1[imid-1],nums2[jmid-1]
            # 右堆最小只有可能是nums1[imid],nums2[jmid]
            # 让左右堆大致相等需要满足的条件是imid+jmid = m-imid+n-jmid 即 jmid = (m+n-2imid)//2
            # 为什么是大致呢？因为有总数为奇数的情况，这里用向下取整数操作，所以如果是奇数，右堆会多1
            jmid = (m + n - 2 * imid) // 2

            # 前面的判断条件只是为了保证不会index out of range
            if imid > 0 and nums1[imid - 1] > nums2[jmid]:
                # imid太大了，这是里精确查找，不是左闭右开，而是双闭区间，所以直接移动一位
                imax = imid - 1
            elif imid < m and nums2[jmid - 1] > nums1[imid]:
                imin = imid + 1
            # 满足条件
            else:
                # 边界情况处理，都是为了不out of index
                # 依次得到左堆最大和右堆最小
                if imid == m:
                    minright = nums2[jmid]
                elif jmid == n:
                    minright = nums1[imid]
                else:
                    minright = min(nums1[imid], nums2[jmid])

                if imid == 0:
                    maxleft = nums2[jmid - 1]
                elif jmid == 0:
                    maxleft = nums1[imid - 1]
                else:
                    maxleft = max(nums1[imid - 1], nums2[jmid - 1])

                # 前面也提过，因为取中间的时候用的是向下取整，所以如果总数是奇数的话，
                # 应该是右边个数多一些，边界的minright就是中位数
                if ((m + n) % 2) == 1:
                    return minright

                # 否则我们在两个值中间做个平均
                return (maxleft + minright) / 2


def findMedianSortedArrays1(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    p, q = 0, 0
    # 获取中位数的索引
    mid = ((m + n) // 2 - 1, (m + n) // 2) if (m + n) % 2 == 0 else ((m + n) // 2, (m + n) // 2)
    li = []
    while p < m and q < n:
        if nums1[p] <= nums2[q]:
            li.append(nums1[p])
            p += 1
        else:
            li.append(nums2[q])
            q += 1
    else:
        if p >= m:
            while q < n:
                li.append(nums2[q])
                q += 1
        else:
            while p < m:
                li.append(nums1[p])
                p += 1
    res = (li[mid[0]] + li[mid[1]]) / 2
    print(li)
    return res


nums1 = [3, 4, 6, 7, 8, 11, 13]
nums2 = [2, 5, 9, 12, 17, 20, 22]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
print(findMedianSortedArrays1(nums1, nums2))
