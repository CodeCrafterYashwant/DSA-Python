# 🔍 Problem: https://leetcode.com/problems/search-insert-position/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def searchInsert(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return (i)
            break
    else:
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return (i)