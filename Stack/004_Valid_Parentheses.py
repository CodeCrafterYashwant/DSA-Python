# 🔍 Problem: https://leetcode.com/problems/valid-parentheses/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack
