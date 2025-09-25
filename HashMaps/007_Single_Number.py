# 🔍 Problem: https://leetcode.com/problems/single-number/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 7 ms


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = {}
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        for i in nums_count:
            if nums_count[i] == 1:
                return i