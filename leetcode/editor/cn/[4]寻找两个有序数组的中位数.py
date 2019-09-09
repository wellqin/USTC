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

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findKth(A, B, k):
            if len(A) == 0:
                return B[k - 1]
            if len(B) == 0:
                return A[k - 1]
            if k == 1:
                return min(A[0], B[0])

            a = A[k // 2 - 1] if len(A) >= k // 2 else None
            b = B[k // 2 - 1] if len(B) >= k // 2 else None

            if b is None or (a is not None and a < b):
                return findKth(A[k // 2:], B, k - k // 2)
            return findKth(A, B[k // 2:], k - k // 2)  # 这里要注意：因为 k/2 不一定 等于 (k - k/2)

        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return findKth(nums1, nums2, n // 2 + 1)
        else:
            smaller = findKth(nums1, nums2, n // 2)
            bigger = findKth(nums1, nums2, n // 2 + 1)
            return (smaller + bigger) / 2.0


nums1 = [3, 4, 6, 7, 8, 11, 13]
nums2 = [2, 5, 9, 12, 17, 20, 22]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
