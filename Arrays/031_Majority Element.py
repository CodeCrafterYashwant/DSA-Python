# 🔍 Problem: https://leetcode.com/problems/majority-element/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 4 ms


def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        newnums = list(set(nums))
        max = 0
        val  = 0
        for i in newnums:
            if nums.count(i) >max:
                max = nums.count(i)
                val = i
        return val