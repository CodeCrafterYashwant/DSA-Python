# 🔍 Problem: https://leetcode.com/problems/roman-to-integer/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def romanToInt(self, s: str) -> int:
        des = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and des[s[i]] < des[s[i + 1]]:
                res += des[s[i + 1]] - des[s[i]]
                i += 2
            else:
                res += des[s[i]]
                i += 1
        return res