# 🔍 Problem: https://leetcode.com/problems/plus-one/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num = num + 1
        num = [int(digit) for digit in str(num)]
        return (num)  
