import ListNode
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
1. Only constant extra memory is allowed.
2. You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        total = 0
        while cur.next is not None:
            cur = cur.next
            total += 1
        total //= k
        #  --p1 p2-----pre cur---
        p1 = dummy
        for _ in range(total):
            p2 = p1.next
            pre, cur, cnt = p1, p2, 1
            while cnt<=k:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
                cnt += 1
            p1.next, p2.next = pre, cur
            p1 = p2
        return dummy.next
