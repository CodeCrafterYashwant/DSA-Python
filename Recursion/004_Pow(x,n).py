# 🔍 Problem: https://leetcode.com/problems/powx-n/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        half = self.myPow(x,n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x