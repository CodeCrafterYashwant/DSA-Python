# 🔍 Problem: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# 🔢 Difficulty: Easy
  

# Method: 1
# ⏱️ Runtime: 0 ms
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k = ''
        j= ''
        for i in word1:
            k = k+i
        for i in word2:
            j = j+i

        if(k==j):
            return True
        else:
            return False
        

# Method: 2
# ⏱️ Runtime: 0 ms
if ''.join(word1) == ''.join(word2):
            return True
        else:
            return False