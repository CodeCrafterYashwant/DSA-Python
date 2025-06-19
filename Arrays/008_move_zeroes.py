# 🔍 Problem: https://leetcode.com/problems/move-zeroes/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 617 ms


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums