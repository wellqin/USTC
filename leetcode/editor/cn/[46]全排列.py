#给定一个没有重复数字的序列，返回其所有可能的全排列。 
#
# 示例: 
#
# 输入: [1,2,3]
#输出:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#] 
#

# 无重复元素全排列问题
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
        