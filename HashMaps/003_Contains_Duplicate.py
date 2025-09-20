# 🔍 Problem: https://leetcode.com/problems/contains-duplicate/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 12 ms


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for value in nums:
            if value in result:
                result[value] += 1
                return True
            else:
                result[value] = 1
        return False