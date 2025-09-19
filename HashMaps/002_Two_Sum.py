# 🔍 Problem: https://leetcode.com/problems/two-sum/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement],i]
            lookup[num] = i