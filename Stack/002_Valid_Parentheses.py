# 🔍 Problem: https://leetcode.com/problems/valid-parentheses/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 57 ms


class Solution:
    def isValid(self, s: str) -> bool:
        prev_len = -1
        while prev_len != len(s):
            prev_len = len(s)
            s = s.replace("()","").replace("[]","").replace("{}","")
        return len(s) == 0