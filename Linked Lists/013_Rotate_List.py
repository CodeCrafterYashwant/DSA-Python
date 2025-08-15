# 🔍 Problem: https://leetcode.com/problems/rotate-list/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms


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