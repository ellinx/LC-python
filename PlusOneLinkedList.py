import ListNode
"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:

Input:
1->2->3

Output:
1->2->4

"""
class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(node):
            if not node:
                return 1
            carry = helper(node.next)
            s = node.val+carry
            node.val = s%10
            carry = s//10
            return carry

        carry = helper(head)
        if carry:
            dummy = ListNode(carry)
            dummy.next = head
            return dummy
        return head
