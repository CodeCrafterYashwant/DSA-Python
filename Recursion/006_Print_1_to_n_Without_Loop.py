# 🔍 Problem: https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1
# ⏱️ Runtime: 0.08 sec
# 🔢 Difficulty: Easy


class Solution:
    def printTillN(self, n):
        if n == 0:
            return
        self.printTillN(n - 1)
        print(n, end=" ")