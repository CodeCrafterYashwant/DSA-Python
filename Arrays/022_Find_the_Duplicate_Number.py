# 🔍 Problem: https://leetcode.com/problems/find-the-duplicate-number/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 279 ms


# Method = 1(Using Binary Search)
def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = sum(num <= mid for num in nums)

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low
