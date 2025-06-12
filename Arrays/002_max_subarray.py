# 🔍 Problem: https://leetcode.com/problems/maximum-subarray/
# 🧠 Approach: One-pass Hash Map
#🔢 Difficulty: Easy
# ⏱️ Runtime: 60 ms


def maxSubArray(self, nums: List[int]) -> int:     
       maxsum = nums[0]
       cursum = 0
       for i in nums:
           if cursum<0:
               cursum = 0
           cursum = cursum + i
           maxsum = max(maxsum,cursum)
       return maxsum
