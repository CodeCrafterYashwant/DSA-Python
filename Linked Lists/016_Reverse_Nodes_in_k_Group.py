# 🔍 Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        given_list = []
        result = []
        curr = head
        while curr:
            given_list.append(curr.val)
            curr = curr.next
        n = len(given_list)
        for i in range(0,n,k):
            chunk = given_list[i:i+k]
            if len(chunk) == k:
                result.extend(chunk[::-1])
            else:
                result.extend(chunk)
        curr = head
        for i in result:
            curr.val = i
            curr = curr.next
        return head