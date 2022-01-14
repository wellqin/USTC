# -*- coding: utf-8 -*-
import random


def quick_sort(nums, l, r):
    if not nums:
        return []
    if l < r:
        p = partition(nums, l, r)
        quick_sort(nums, l, p - 1)
        quick_sort(nums, p + 1, r)
    return nums


def partition(nums, l, r):
    ran_i = random.randint(l, r)
    nums[ran_i], nums[r] = nums[r], nums[ran_i]
    x = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def main():
    nums = [-1, 19, 2, 13, 8, 34, 25, 7]
    print(quick_sort(nums, 0, len(nums) - 1))


if __name__ == "__main__":
    main()
