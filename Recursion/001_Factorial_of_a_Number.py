# 🔍 Problem: https://www.geeksforgeeks.org/problems/factorial5739/1

# Method = 1
# ⏱️ Runtime: 0 ms
# 🔢 Difficulty: Easy
class Solution:
    def factorial (self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)
    

# Method = 2
# ⏱️ Runtime: 0 ms
# 🔢 Difficulty: Medium
class Solution:
    def factorial(self, n, acc=1):
        if n == 0:
            return acc
        return self.factorial(n-1, acc * n)
