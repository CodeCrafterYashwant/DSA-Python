# 🔍 Problem: https://leetcode.com/problems/reverse-string/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 4 ms


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left,right):
            if left>=right:
                return
            s[left],s[right] = s[right],s[left]
            helper(left+1,right-1)
        return helper(0,len(s)-1)