# 🔍 Problem: https://leetcode.com/problems/swap-nodes-in-pairs/


# Method = 1
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 0 ms
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dummy.next
    

# Method = 2
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        numbers = []
        while curr:
           numbers.append(curr.val)
           curr = curr.next
        start = 0
        sec_start = 1   
        while sec_start < len(numbers):
            temp = numbers[start]
            numbers[start] = numbers[sec_start]
            numbers[sec_start] = temp
            start = start + 2
            sec_start = sec_start +2
        curr = head
        for i in numbers:
            curr.val = i
            curr = curr.next
        return head