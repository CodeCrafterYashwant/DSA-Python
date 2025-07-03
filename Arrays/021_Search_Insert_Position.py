# 🔍 Problem: https://leetcode.com/problems/search-insert-position/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


# Method = 1(Binary Search)
def searchInsert(self, nums: List[int], target: int) -> int:
        left ,right = 0,len(nums)-1
        while left<= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return (mid)        
            elif nums[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        return (left)


# Method = 2
def searchInsert(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return (i)
            break
    else:
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return (i)