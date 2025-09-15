# 🔍 Problem: https://leetcode.com/problems/sort-an-array/
# 🔢 Difficulty: Easy


# Method = 1
# ⏱️ Runtime: 23 ms
def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


# Method = 2
# ⏱️ Runtime: 18 ms
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)