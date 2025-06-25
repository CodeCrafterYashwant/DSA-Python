# 🔍 Problem: https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
# 🔢 Difficulty: Easy
# ⏱️ Time Taken: 0.34


def get_min_max(self, arr):
        arr.sort()
        return arr[0],arr[-1]
    