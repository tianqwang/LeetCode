#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i,num in enumerate(nums):
            if (target-num) in seen.keys():
                return i, seen[target-num]
            if num not in seen.keys():
                seen[num] = i
        return 'no solution'

