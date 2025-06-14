# 🔍 Problem: https://leetcode.com/problems/two-sum/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 3 ms


def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        print(i,num)
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

