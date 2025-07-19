# 🔍 Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 275 ms


def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            temp = ''
            for j in range(i,len(s)):
                if s[j] not in temp:
                    temp = temp + s[j]
                    if len(temp) > longest:
                        longest = len(temp)
                else:
                    break
        return longest