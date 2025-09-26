# 🔍 Problem: https://leetcode.com/problems/happy-number/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n!= 1:
            if n in seen:
                return False
            seen[n] = True
            n = sum(int(digit) ** 2 for digit in str(n))
        return True