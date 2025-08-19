# 🔍 Problem: https://leetcode.com/problems/reverse-linked-list/
# 🔢 Difficulty: Easy


# Method = 1
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
    

# Method = 2
# ⏱️ Runtime: 0 ms
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        all_members = []
        curr = head
        lenght = 0
        while curr:
            all_members.append(curr.val)
            curr = curr.next
            lenght = lenght + 1
        index = lenght - n
        all_members.pop(index)
        dummy = ListNode()
        curr = dummy
        for i in all_members:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next