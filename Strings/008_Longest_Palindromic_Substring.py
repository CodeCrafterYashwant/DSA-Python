# 🔍 Problem: https://leetcode.com/problems/longest-palindromic-substring/
# 🔢 Difficulty: Medium


# ⏱️ Runtime: 8575 ms
#M-1 Bruthforce
def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                k = s[i:j+1]
                r = k[::-1]
                if k == r:
                    if len(r) > len(res):
                        res = r
        return res