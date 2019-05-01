#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        ntag = 0
        if x<0:
            ntag = True
        x = abs(x)
        output = 0
        while x!=0:
            lst = x%10
            output = output*10 + lst
            x = int(x/10)
        if output>(2**31-1):
            return 0
        if ntag==True:
            return -output
        return output
             


