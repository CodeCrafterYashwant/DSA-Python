# 🔍 Problem: https://leetcode.com/problems/smallest-even-multiple/
# 🔢 Difficulty: Easy


# Method = 1
# ⏱️ Runtime: 0 ms
def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2 == 0 else n*2


# Method = 2
# ⏱️ Runtime: 27 ms
def smallestEvenMultiple(self, n: int) -> int:
        nums2 = [2*i for i in range(1,151)]
        numsn = [n*i for i in range(1,151)]
        res = []
        for i in nums2:
            for j in numsn:
                if i == j:
                    res.append(i)
                if len(res) == 1:
                    break
        return (res[0])