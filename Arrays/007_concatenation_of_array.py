# 🔍 Problem: https://leetcode.com/problems/concatenation-of-array/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def getConcatenation(self, nums: List[int]) -> List[int]:
       k = []
       k = nums.copy()
       k.extend(nums)
       return k
        