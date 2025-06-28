# 🔍 Problem: https://leetcode.com/problems/container-with-most-water/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 105 ms


# Method = 1(Brute force)
def maxArea(self, height: List[int]) -> int:
    res = 0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            area = (j-i) * min(height[i],height[j])
            res = max(res,area)
    return res


# METHOD = 2 (O(n) time, O(1) space)
def maxArea(self, height: List[int]) -> int:
        res = 0
        l ,r = 0,len(height) - 1
        while r>l:
            area = (r-l) * min(height[l],height[r])
            res = max(res,area)
            if height[l]>height[r]:
                r -= 1
            else:
                l += 1
        return res