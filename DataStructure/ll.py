# -*- coding:utf-8 -*-

# n = int(input())
# lit = list(map(int, input().split()))
# li = []
# for i in range(n - 1):
#     b = list(map(int, input().split()))
#     li.append(b)
#
# print(n - 1)


ll = [1,1,1,1]
n = 4
c = 2
s = 2

# ll = [1,2,3,1]
# n = 4
# c = 2
# s = 2

# res = 0
# for i in range(len(ll) - s + 1):
#     if max(ll[i:i+s]) <= c:
#         res += 1
# print(res)


class Solution:
    def __init__(self):
        self.real_s = ""
        self.input = "R))LL(((RR)"
        self.index = 0

    def L(self):
        self.index -= 1
        return self.real_s, self.index

    def R(self):
        self.index += 1
        return self.real_s, self.index

    def D(self):
        if self.index >= len(self.real_s):
            self.real_s = self.real_s[:-1]  # 考虑中间位置删除
        else:
            self.real_s = self.real_s[:self.index] + self.real_s[self.index + 1:]
        self.index = self.index - 1
        return self.real_s, self.index

    def LC(self):
        split_strings = self.real_s.split()
        split_strings.insert(self.index, "(")
        self.real_s = ' '.join(split_strings)
        self.index += 1
        return self.real_s, self.index

    def RC(self):
        split_strings = self.real_s.split()
        split_strings.insert(self.index, ")")
        self.real_s = ' '.join(split_strings)
        self.index += 1
        return self.real_s, self.index

    def combine(self, ss):
        # 括号嵌套深度
        ans = 0
        now = 0
        for ch in ss:
            if ch == "(":
                now += 1
                ans = max(ans, now)
            elif ch == ")":
                now -= 1
        return ans

    def calc_string(self):
        ss = ""
        index = 0
        for i in self.input:
            if i in "RLD":
                print(0)
            else:
                break
        self.input = self.input.lstrip("RLD")
        # "R))LL(((RR)"
        for i in self.input:
            if i == "(":
                ss, index = self.LC()
            if i == ")":
                ss, index = self.RC()
            if i == "R":
                ss, index = self.R()
            if i == "L":
                ss, index = self.L()
            if i == "D":
                ss, index = self.D()
            ss = ss.replace(' ', '')
            ll = self.combine(ss)
            print(ss, index, self.combine(ss))
            # print(ll * 2 - len(ss))
            # print(self.combine(ss))
            print(ss)
            if (ll * 2 - len(ss)) == 0:
                print(ll)
            else:
                print(ll * 2 - len(ss))


Solution().calc_string()
