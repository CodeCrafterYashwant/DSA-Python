# 🔍 Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Method = 1
# ⏱️ Runtime: 0 ms
# 🔢 Difficulty: Medium
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
    

# Method = 2
# ⏱️ Runtime: 14 ms
# 🔢 Difficulty: Medium
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        data = []
        while curr:
            data.append(curr.val)
            curr = curr.next
        curr = head
        unique = [x for x in data if data.count(x) == 1]
        dummy = ListNode(0)
        head = dummy
        curr = head
        for i in unique:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next