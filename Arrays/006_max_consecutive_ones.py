# 🔍 Problem: https://leetcode.com/problems/max-consecutive-ones/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 45 ms


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_run = curr = nums[0] if nums else 0
        for current, nxt in zip(nums, nums[1:]):
            if nxt == 1:
                curr += 1 if current == 1 else 1
            else:
                curr = 0
            max_run = max(max_run, curr)
        # Handle case where array has only one element
        if len(nums) == 1:
            return nums[0]
        return max_run
