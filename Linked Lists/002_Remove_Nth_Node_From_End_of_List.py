# 🔍 Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length = length+1
            curr = curr.next
        if n == length:
            return head.next
        curr = head
        for i in range(length-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head