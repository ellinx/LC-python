"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterative
        pre = None
        cur = head
        while cur:
            nextCur = cur.next
            cur.next = pre
            pre, cur = cur, nextCur
        return pre

class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #recursive
        def helper(head):
            pre, cur = head, head.next
            if cur is None:
                return [head,head]
            rh, rt = helper(cur)
            rt.next = pre
            pre.next = None
            return [rh, pre]

        if head is None:
            return None
        return helper(head)[0]
