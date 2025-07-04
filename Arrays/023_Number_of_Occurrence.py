# 🔍 Problem: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
# 🔢 Difficulty: Easy


# Method = 1
# ⏱️ Time Taken: 0.32

def countFreq(self, arr, target):
        occ = 0
        for i in arr:
            if i == target:
                occ = occ +1
        return occ


# Method = 2
# ⏱️ Time Taken: 0.41

def countFreq(self, arr, target):
        return arr.count(target)