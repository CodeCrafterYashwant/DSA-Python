# 🔍 Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1