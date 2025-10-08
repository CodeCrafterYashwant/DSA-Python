# 🔍 Problem: https://leetcode.com/problems/reverse-string/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in s:
            stack.append(i)
        for i in range(len(s)):
            s[i] = stack.pop()
