# 🔍 Problem: https://leetcode.com/problems/contiguous-array/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 90 ms


class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        max_len = 0
        hashmap = {0: -1}  
        for i, num in enumerate(nums):
            prefix_sum += -1 if num == 0 else 1

            if prefix_sum in hashmap:
                max_len = max(max_len, i - hashmap[prefix_sum])
            else:
                hashmap[prefix_sum] = i

        return max_len
