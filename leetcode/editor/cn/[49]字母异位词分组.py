#给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
#
# 示例: 
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
#输出:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#] 
#
# 说明： 
#
# 
# 所有输入均为小写字母。 
# 不考虑答案输出的顺序。 
# 
# Related Topics 哈希表 字符串



#leetcode submit region begin(Prohibit modification and deletion)
# 每一个字符串都先排个序看看是不是一样，这样更好判断

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapx = {}
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in mapx:
                mapx[tmp].append(i)
            else:
                mapx[tmp] = [i]
        return mapx.values()
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(s))
#leetcode submit region end(Prohibit modification and deletion)
