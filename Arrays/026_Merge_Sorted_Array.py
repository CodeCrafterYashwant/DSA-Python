# 🔍 Problem: https://leetcode.com/problems/merge-sorted-array/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
          nums1[m+j] = nums2[j]
        nums1.sort()