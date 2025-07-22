# 🔍 Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 4 ms
  

def reverseWords(self, s: str) -> str:
        s = s.split()
        result = ''
        for i in s:
            i = i[::-1]  
            result = result + i + ' '
        return result.strip()