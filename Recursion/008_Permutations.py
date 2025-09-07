# 🔍 Problem: https://leetcode.com/problems/permutations/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path,remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])
                path.pop()
        backtrack([],nums)
        return res