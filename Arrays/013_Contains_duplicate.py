# 🔍 Problem: https://leetcode.com/problems/contains-duplicate/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 13 ms


def containsDuplicate(self, nums: List[int]) -> bool:
        k = set()
        for i in nums:
            if i in k:
                return True
            k.add(i)     
        return False