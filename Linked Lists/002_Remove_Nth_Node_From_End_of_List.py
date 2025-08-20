# 🔍 Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 🔢 Difficulty: Medium

# Method = 1
# ⏱️ Runtime: 0 ms
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
    

    
# Method = 3
# ⏱️ Runtime: 0 ms
class Solution:
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next