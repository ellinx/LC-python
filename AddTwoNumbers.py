"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        c = 0
        while l1 is not None and l2 is not None:
            s = l1.val+l2.val+c
            c = s//10
            s %= 10
            cur.next = ListNode(s)
            cur, l1, l2 = cur.next, l1.next, l2.next
        while l1 is not None:
            s = l1.val+c
            c = s//10
            s %= 10
            cur.next = ListNode(s)
            cur, l1 = cur.next, l1.next
        while l2 is not None:
            s = l2.val+c
            c = s//10
            s %= 10
            cur.next = ListNode(s)
            cur, l2 = cur.next, l2.next
        if c>0:
            cur.next = ListNode(c)
        return dummy.next
