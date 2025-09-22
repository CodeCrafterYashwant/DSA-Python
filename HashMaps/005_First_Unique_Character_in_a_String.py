# 🔍 Problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 63 ms


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for i,char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1
