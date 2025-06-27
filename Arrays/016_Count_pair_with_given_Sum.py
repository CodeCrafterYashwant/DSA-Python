# 🔍 Problem: https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum--150253/1
# 🔢 Difficulty: Medium
# ⏱️ Time Taken: 0.08


def countPairs(self,arr, target):
        count = 0
        freq = {}
        
        for num in arr:
            rem = target - num
            if rem in freq:
                count += freq[rem]
            freq[num] = freq.get(num, 0) + 1
        
        return (count)
