# 🔍 Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr != None and curr.next !=None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head