# 🔍 Problem: https://leetcode.com/problems/subarray-sum-equals-k/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 26 ms


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        m = {0: 1}
        for n in nums:
            s += n
            count += m.get(s - k, 0)
            m[s] = m.get(s, 0) + 1
        return count