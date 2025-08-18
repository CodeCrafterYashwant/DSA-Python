# 🔍 Problem: https://leetcode.com/problems/add-two-numbers/
# 🔢 Difficulty: Medium

# Method = 1
# ⏱️ Runtime: 0 ms
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total//10
            total = total % 10
            curr.next = ListNode(total)
            curr = curr.next
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
        return dummy.next
    

# Method = 2
# ⏱️ Runtime: 3 ms
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2 = [],[]
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num1 = int(''.join(map(str,num1[::-1])))
        num2 = int(''.join(map(str,num2[::-1])))
        result = str(num1 + num2)
        dummy = ListNode()
        curr = dummy
        for i in result[::-1]:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next
    


# Method = 3
# ⏱️ Runtime: 9 ms
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2 = [],[]
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num1 = int(''.join(map(str,num1[::-1])))
        num2 = int(''.join(map(str,num2[::-1])))
        result = str(num1 + num2)
        res = []
        for i in (result[::-1]):
            res.append(i)
        dummy = ListNode()
        curr = dummy
        for i in res:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next
