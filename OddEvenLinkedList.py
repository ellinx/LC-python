"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
1. The relative order inside both the even and odd groups should remain as it was in the input.
2. The first node is considered odd, the second node even and so on ...
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def process(head):
            if head is None:
                return [None]*2
            if head.next is None:
                return [head, None]
            ret = [head, head.next]
            odd, even = process(head.next.next)
            ret[0].next, ret[1].next = odd, even
            return ret

        odd, even = process(head)
        if odd is None:
            return None
        cur = odd
        while cur.next is not None:
            cur = cur.next
        cur.next = even
        return odd
