# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        电话号码
Description :   
Author :          wellqin
date:             2019/9/16
Change Activity:  2019/9/16
-------------------------------------------------
"""
class Solution:
    def numberCombind(self, num):
        dicts = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "s", "y", "s"]
        }
        ans = []
        def combind(s, num):
            if len(num) == 0:
                ans.append(s)
            else:
                cur = num[0]
                for i in dicts[cur]:
                    combind(s + i, num[1:])
            return ans
        if not num or len(num) == 0:
            return []
        combind('', num)
        return ans

num = str(input())
# num = "23"
result = []
res = Solution().numberCombind(num)
print(res)
for i in res:
    print(type(i))
    result.append(i)
print(result)




