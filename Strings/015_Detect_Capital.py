# 🔍 Problem: https://leetcode.com/problems/detect-capital/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word == word.capitalize():
            return True
        else:
            return False