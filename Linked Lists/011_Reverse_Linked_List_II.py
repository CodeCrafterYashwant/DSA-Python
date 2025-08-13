# 🔍 Problem: https://leetcode.com/problems/reverse-linked-list-ii/
# 🔢 Difficulty: Easy


# Method = 1
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
    

# Method = 2
# ⏱️ Runtime: 0 ms
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head     
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy   
        for _ in range(left - 1):
            prev = prev.next     
        curr = prev.next
        next_node = None       
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node        
        return dummy.next