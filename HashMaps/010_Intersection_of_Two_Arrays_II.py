# 🔍 Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_count = {}
        nums2_count = {}
        for num in nums1:
            if num in nums1_count:
                nums1_count[num] += 1
            else:
                nums1_count[num] = 1
        for num in nums2:
            if num in nums2_count:
                nums2_count[num] += 1
            else:
                nums2_count[num] = 1
        for num in nums1_count:
            if num in nums2_count:
                minimum_count = min(nums1_count[num],nums2_count[num])
                for _ in range(minimum_count):
                    result.append(num)

        return (result)