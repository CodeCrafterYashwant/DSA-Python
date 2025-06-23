# 🔍 Problem: https://www.geeksforgeeks.org/problems/second-largest3735/1
# 🔢 Difficulty: Easy
# ⏱️ Time Taken: 0.24


def getSecondLargest(self, arr):
    # Code Here
    k = set()
    for i in arr:
        k.add(i)
    l = list(k)
    l.sort(),l.reverse()
    if len(l) == 1:
        return -1
    else:
        return (l[1])