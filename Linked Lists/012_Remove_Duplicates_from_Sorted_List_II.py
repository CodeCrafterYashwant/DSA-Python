# 🔍 Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        freq = {}
        curr = head
        while curr:
            freq[curr.val] = freq.get(curr.val, 0) + 1 
            curr = curr.next
        dummy = ListNode(0)
        curr = dummy
        temp = head
        while temp:
            if freq[temp.val] == 1: 
                curr.next = ListNode(temp.val)
                curr = curr.next
            temp = temp.next
        return dummy.next