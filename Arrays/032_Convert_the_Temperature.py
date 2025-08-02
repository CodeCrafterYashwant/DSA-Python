# 🔍 Problem: https://leetcode.com/problems/convert-the-temperature/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def convertTemperature(self, celsius: float) -> List[float]:
        result = []
        K = celsius + 273.15
        F = (celsius * 9/5) + 32
        result.append(K)
        result.append(F)
        return result