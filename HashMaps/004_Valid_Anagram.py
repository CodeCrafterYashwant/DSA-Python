# 🔍 Problem: https://leetcode.com/problems/valid-anagram/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 11 ms


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1
        for ch in t:
            if ch in char_count:
                char_count[ch] -= 1
            else:
                char_count[ch] = -1
        for count in char_count.values():
            if count != 0:
                return False
        return True