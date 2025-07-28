# 🔍 Problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 31 ms


class ListNode:
    def __init__(self, val = 0,next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

