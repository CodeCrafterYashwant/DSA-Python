# 🔍 Problem: https://leetcode.com/problems/reverse-string/
# 🔢 Difficulty: Easy


# ⏱️ Runtime: 0 ms
def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left,right = 0,len(s)-1
        while (left<right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



# ⏱️ Runtime: 0 ms
def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()