# 🔍 Problem: https://leetcode.com/problems/merge-two-sorted-lists/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2