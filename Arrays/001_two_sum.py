# 🔍 Problem: https://leetcode.com/problems/two-sum/
# 🧠 Approach: One-pass Hash Map
#🔢 Difficulty: Easy | Medium | Hard
# ⏱️ Time Complexity:



def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
