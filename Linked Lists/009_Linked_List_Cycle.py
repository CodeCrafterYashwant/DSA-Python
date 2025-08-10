# 🔍 Problem: https://leetcode.com/problems/linked-list-cycle/
# 🔢 Difficulty: Easy

# Method = 1
# ⏱️ Runtime: 42 ms
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        k = set()
        while head:
            if head in k:
                return True
            k.add(head)
            head = head.next
        return False


# Method = 2 (Floyd's Cycle Detection algorithm)
# ⏱️ Runtime: 35 ms
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False