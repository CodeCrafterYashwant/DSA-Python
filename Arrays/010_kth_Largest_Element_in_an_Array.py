# 🔍 Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 59 ms


def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        return (nums[k-1])
        