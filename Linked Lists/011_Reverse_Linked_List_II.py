# 🔍 Problem: https://leetcode.com/problems/reverse-linked-list-ii/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        val = []
        curr = head
        while curr:
            val.append(curr.val)
            curr = curr.next
        val[left-1:right] = val[left-1:right][::-1]
        curr = head
        for v in val:
            curr.val = v
            curr = curr.next
        return head