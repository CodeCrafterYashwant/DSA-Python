# 🔍 Problem: https://leetcode.com/problems/reorder-list/
# 🔢 Difficulty: Easy–Medium
# ⏱️ Runtime: 0 ms


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        numbers = []
        curr = head
        while curr:
            numbers.append(curr.val)
            curr = curr.next
        
        first = 0
        last = len(numbers) - 1
        res = []
        while first<=last:
            if first == last:
                res.append(numbers[first])
            else:
                res.append(numbers[first])
                res.append(numbers[last])
            first += 1
            last -= 1

        curr = head
        for num in res:
            curr.val = num
            curr = curr.next
        