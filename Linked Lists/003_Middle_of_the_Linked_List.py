# 🔍 Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length = length + 1
            curr = curr.next
        curr = head
        mid = (length//2) 
        for i in range(mid):
            curr = curr.next
        return curr