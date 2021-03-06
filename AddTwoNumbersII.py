"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def helper(l):
            ret = ""
            while l is not None:
                ret += str(l.val)
                l = l.next
            return ret

        s = int(helper(l1))+int(helper(l2))
        dummy = ListNode(0)
        cur = dummy
        for c in str(s):
            cur.next = ListNode(int(c))
            cur = cur.next
        return dummy.next
