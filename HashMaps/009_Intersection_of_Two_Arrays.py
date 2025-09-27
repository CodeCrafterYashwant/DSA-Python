# 🔍 Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_count = {}
        num2_count = {}
        result = []
        for num in nums1:
            if num in num1_count:
                num1_count[num] += 1
            else:
                num1_count[num] = 1
        for num in nums2:
            if num in num2_count:
                num2_count[num] += 1
            else:
                num2_count[num] = 1
        if len(num1_count) < len(num2_count):
            for i in num1_count:
                if i in num2_count:
                    result.append(i)
        else:
            for i in num2_count:
                if i in num1_count:
                    result.append(i)
        return result