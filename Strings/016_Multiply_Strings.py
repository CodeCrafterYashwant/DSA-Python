# 🔍 Problem: https://leetcode.com/problems/multiply-strings/

# Method = 1: Using built-in conversion functions 
# 🔢 Difficulty: Very Easy
# ⏱️ Runtime: 0 ms
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    

# Method = 2: Without using built-in conversion functions
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 30 ms
class Solution: 
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"    
        result = [0] * (len(num1) + len(num2))   
        num1 = num1[::-1]
        num2 = num2[::-1]      
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                result[i + j] += mul
                result[i + j + 1] += result[i + j] // 10  
                result[i + j] %= 10          
        while result[-1] == 0:
            result.pop()    
        return ''.join(map(str, result[::-1]))