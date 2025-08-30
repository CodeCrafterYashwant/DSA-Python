# 🔍 Problem: https://leetcode.com/problems/reverse-string/


# Method = 1
# ⏱️ Runtime: 4 ms
# 🔢 Difficulty: Easy
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left,right):
            if left>=right:
                return
            s[left],s[right] = s[right],s[left]
            helper(left+1,right-1)
        return helper(0,len(s)-1)


# Method = 2
# ⏱️ Runtime: 3 ms
# 🔢 Difficulty: Easy
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(i):
            if i>=len(s) // 2:
                return
            s[i],s[-i-1] = s[-i-1],s[i]
            helper(i+1)
        return helper(0)