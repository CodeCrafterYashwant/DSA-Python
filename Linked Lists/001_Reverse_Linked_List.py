# 🔍 Problem: https://leetcode.com/problems/reverse-linked-list/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next    
            curr.next = prev       
            prev = curr             
            curr = next_node

        return prev