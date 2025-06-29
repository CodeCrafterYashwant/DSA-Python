# 🔍 Problem: https://leetcode.com/problems/rotate-array/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 1371 ms

def rotate(self, nums: List[int], k: int) -> None:
    for i in range(k):
        nums.insert(0,nums[-1])
        nums.pop()
    return (nums)
