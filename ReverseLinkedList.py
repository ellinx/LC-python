"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p0, p1, p2 = None, head, head.next
        while p2 is not None:
            p3 = p2.next
            p1.next, p2.next = p0, p1
            p0, p1, p2 = p1, p2, p3
        return p1

class Solution2:
    #recursive
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        p1, p2 = head, head.next
        ret = self.reverseList(p2)
        p2.next, p1.next = p1, None
        return ret
