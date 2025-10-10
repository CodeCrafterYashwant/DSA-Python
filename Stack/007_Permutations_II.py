# 🔍 Problem: https://leetcode.com/problems/permutations-ii/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 5 ms


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        stack = [([], [False] * len(nums), 0)] 
        while stack:
            path, used, depth = stack.pop()
            if len(path) == len(nums):
                res.append(path)
                continue
            for i in range(len(nums)-1, -1, -1): 
                if used[i]:
                    continue
                if i < len(nums) - 1 and nums[i] == nums[i + 1] and not used[i + 1]:
                    continue
                new_path = path + [nums[i]]
                new_used = used[:]
                new_used[i] = True
                stack.append((new_path, new_used, depth + 1))
        return res
