# 🔍 Problem: https://leetcode.com/problems/single-number/
# 🔢 Difficulty: Easy

# Method - 1
# ⏱️ Runtime: 0 ms
def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result =  result ^ i 
        return result



# Method - 2
# ⏱️ Runtime: 3 ms
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from operator import xor
    return reduce(xor, nums)



# Method - 3
# ⏱️ Runtime: 5382 ms
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return (nums[i])