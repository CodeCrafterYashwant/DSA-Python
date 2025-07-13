# 🔍 Problem: https://leetcode.com/problems/valid-anagram/
# 🔢 Difficulty: Easy



# ⏱️ Runtime: 215 ms
def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(s) == len(t):
            for i in s:
                if i in t:
                    t = t.replace(i,"",1)
                    count = count + 1
        if count == len(s):
            return True
        else:
            return False
        


# ⏱️ Runtime: 19 ms
def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False