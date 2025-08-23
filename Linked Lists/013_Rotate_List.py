# 🔍 Problem: https://leetcode.com/problems/rotate-list/



#Method = 1
# ⏱️ Runtime: 0 ms
# 🔢 Difficulty: Easy
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        length = len(vals)
        if k == 0 or length == 0:
            return head
        else:
            k = k % length
            vals = vals[-k:] + vals[:-k]
            dummy = ListNode(0)
            head = dummy
            curr = head
            for i in vals:
                curr.next = ListNode(i)
                curr = curr.next
            return dummy.next
        

#Method = 2
# ⏱️ Runtime: 0 ms
# 🔢 Difficulty: Medium
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return head
        tail.next = head
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
