# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        验证ip地址
Description :   
Author :          wellqin
date:             2019/9/16
Change Activity:  2019/9/16
-------------------------------------------------
"""
# 验证ip地址
import sys
class Solution:
    def vaild_ipaddr(self, str):
        ip = str.split('.')
        if len(ip) == 4:
            for i in range(4):
                length = len(ip[i])

                if length > 3 or length ==0:
                    return "Neither"

                if length>1:
                    if not ("1" <=ip[i][0] <= "9"):
                        return "Neither"

                for j in range(length):
                    if not ("1" <=ip[i][j] <= "9"):
                        return "Neither"
                if int(ip[i]) > 255:
                    return "Neither"
            return "IPV4"

        ips = str.split(':')
        if len(ips) == 8:
            for i in range(8):
                length = len(ips[i])

                if length > 4 or length == 0:
                    return "Neither"

                for j in range(length):
                    if not ("1" <= ip[i][j] <= "9" or "a" <= ip[i][j] <= "f" or "A" <= ip[i][j] <= "F"):
                        return "Neither"
            return "IPV6"

        return "Neither"


str = sys.stdin.readline().strip()
print(Solution().vaild_ipaddr(str))