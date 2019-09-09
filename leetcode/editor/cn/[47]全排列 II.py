#给定一个可包含重复数字的序列，返回所有不重复的全排列。 
#
# 示例: 
#
# 输入: [1,1,2]
#输出:
#[
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
#] 
#

# 无重复元素全排列问题
"""
这里我们应该使用计数器记录nums中每个元素出现的次数，如果当前元素超过次数则返回，
但是这里还有一个问题就是可能会出现同样的排列多次，这里的解决办法就是同一层不许出现重复元素，
这里有两种解决办法，一种是直接传入distinct的数组，还有一种是使用一个集合记录当前层已使用的元素。
"""

class Solution(object):
    def backtrack(self,nums):
        if not nums:
            return []
        res = []

        # res用来存储所有的返回所有排列，templist用来生成每个排列
        def helper(res, templist, nums):
            if (len(templist) == len(nums)):
                res.append(templist[:])
            else:
                for i in nums:
                    if i in templist:  # 如果在当前排列中已经有i了，就continue，相当于分支限界，即不对当前节点子树搜寻了
                        continue
                    templist.append(i)
                    helper(res, templist, nums)
                    templist.pop()  # 把结尾的元素用nums中的下一个值替换掉，遍历下一颗子树

        helper(res, [], nums)
        return res

nums = [1,2,3]
print(Solution().backtrack(nums))


from collections import Counter
class Solution1(object):

    def backtrack(self, nums):

        res, tmplist, counter = [], [], Counter(nums)
        length = len(nums)

        def helper(res, tmplist, counter, nums, length):
            if len(tmplist) == length:  # 回溯点
                res.append(tmplist[:])
            else:
                for i in nums:  # 横向遍历
                    if counter[i] == 0:  # 分支限界
                        continue

                    counter[i] -= 1
                    tmplist.append(i)
                    helper(res, tmplist, counter, nums, length)  # 纵向遍历
                    counter[i] += 1
                    tmplist.pop()

        helper(res, tmplist, counter, list(set(nums)), length) # 同一层不许出现重复元素,使用一个集合记录当前层已使用的元素。直接传入distinct的数组

        return res

nums = [1,1,2]
print(Solution1().backtrack(nums))

        