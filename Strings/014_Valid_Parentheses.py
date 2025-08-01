# 🔍 Problem: https://leetcode.com/problems/valid-parentheses/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def isValid(self, s: str) -> bool:
        k = []  
        for i in s:
            if i in "({[":
                k.append(i)
            else:
                if not k:
                    return False
                last = k.pop()
                if i == ')' and last != '(':
                    return False
                if i == ']' and last != '[':
                    return False
                if i == '}' and last != '{':
                    return False
        return len(k) == 0
