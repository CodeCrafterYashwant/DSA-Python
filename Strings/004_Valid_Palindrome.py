# 🔍 Problem: https://leetcode.com/problems/valid-palindrome/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 4 ms


def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        k = ''.join(c for c in s if c.isalnum())
        r = k[::-1]
        if r == k:
            return True
        else:
            return False