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
        stk1, stk2 = collections.deque(), collections.deque()
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        stk = collections.deque()
        carry = 0
        while len(stk1) and len(stk2):
            s = stk1.pop() + stk2.pop() + carry
            carry = s//10
            stk.append(s%10)
        while len(stk1):
            s = stk1.pop() + carry
            carry = s//10
            stk.append(s%10)
        while len(stk2):
            s = stk2.pop() + carry
            carry = s//10
            stk.append(s%10)
        if carry:
            stk.append(carry)
        dummy = TreeNode(0)
        cur = dummy
        while len(stk):
            cur.next = ListNode(stk.pop())
            cur = cur.next
        return dummy.next
