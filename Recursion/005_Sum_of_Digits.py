# 🔍 Problem: Sum of Digits of any integer
# 🔢 Difficulty: Easy


class Solution:
    def sum_of_digits(n: int) -> int:
        if n == 0:
            return 0
        else:
            return (n % 10) + sum_of_digits(n // 10)
        