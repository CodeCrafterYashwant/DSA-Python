# 🔍 Problem: https://leetcode.com/problems/find-the-difference/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 1 ms


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}
        for char in t:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in s:
            if char in s:
                char_count[char] -=1
        for char in char_count:
            if char_count[char] == 1:
                return char