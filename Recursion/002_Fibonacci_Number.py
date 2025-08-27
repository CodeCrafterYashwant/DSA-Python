# 🔍 Problem: https://leetcode.com/problems/fibonacci-number/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 35 ms


class Solution:
    def __init__(self):
            self.memo = {}
    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]