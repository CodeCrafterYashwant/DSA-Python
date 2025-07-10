# 🔍 Problem: https://leetcode.com/problems/longest-consecutive-sequence/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 45 ms


def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longestSeq = 0
        for num in nums:
            if (num -1) not in nums:
                length = 0
                while num + length in nums:
                    length += 1
                longestSeq = max(longestSeq,length)
        return longestSeq