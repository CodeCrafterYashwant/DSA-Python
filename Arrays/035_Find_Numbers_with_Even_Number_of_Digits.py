# 🔍 Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# 🔢 Difficulty: Easy


# Method = 1
# ⏱️ Runtime: 0 ms
def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                result = result + 1
        return result


# Method = 2
# ⏱️ Runtime: 3 ms
 def findNumbers(self, nums: List[int]) -> int:
        dct = {}
        freq = 0
        result = 0
        for i in nums:
            for j in str(i):
                freq = freq+1
            dct[i] = freq
            freq = 0
            if dct[i] %2 == 0:
                result += 1
        return (result)