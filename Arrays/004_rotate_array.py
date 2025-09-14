# 🔍 Problem: https://leetcode.com/problems/rotate-array/
# 🔢 Difficulty: Medium


#Method = 1
# ⏱️ Runtime: 3 ms
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(start,end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)


#Method = 2
# ⏱️ Runtime: 1371 ms
def rotate(self, nums: List[int], k: int) -> None:
    for i in range(k):
        nums.insert(0,nums[-1])
        nums.pop()
    return (nums)
