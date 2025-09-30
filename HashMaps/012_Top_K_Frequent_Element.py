# 🔍 Problem: https://leetcode.com/problems/top-k-frequent-elements/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 3 ms


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        freq_list = []
        for num in freq:
            freq_list.append((num,freq[num]))
        freq_list.sort(key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
        return (result)