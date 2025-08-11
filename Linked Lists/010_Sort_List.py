# 🔍 Problem: https://leetcode.com/problems/sort-list/
# 🔢 Difficulty: Easy–Medium
# ⏱️ Runtime: 7 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head
        val = []
        curr = head
        while curr:
            val.append(curr.val)
            curr = curr.next
        val.sort()
        curr = head
        for i in val:
            curr.val = i
            curr = curr.next
        return head