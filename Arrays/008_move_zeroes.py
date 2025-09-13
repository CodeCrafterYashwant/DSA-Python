# 🔍 Problem: https://leetcode.com/problems/move-zeroes/
# 🔢 Difficulty: Easy

#Method = 1
# ⏱️ Runtime: 3 ms
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1
        for i in range(position,len(nums)):
            nums[i] = 0


#Method = 2
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