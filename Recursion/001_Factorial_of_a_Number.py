# 🔍 Problem: https://www.geeksforgeeks.org/problems/factorial5739/1
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def factorial (self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)