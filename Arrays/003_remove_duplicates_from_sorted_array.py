# 🔍 Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 🧠 Approach: One-pass Hash Map
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0    
    k = 0
    for i in range(1,len(nums)):
            if nums[k] != nums[i]:
                k = k+1
            nums[k] = nums[i]
    return k+1