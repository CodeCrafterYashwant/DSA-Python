# 🔍 Problem: https://leetcode.com/problems/rotate-string/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms

def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)