# 🔍 Problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 67 ms
  

def firstUniqChar(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1 