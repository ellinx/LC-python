"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        p1, p2, p3, p4 = None, None, None, None
        idx = 0
        while idx<m-1:
            idx += 1
            cur = cur.next
        p1 = cur
        idx += 1
        cur = cur.next
        p2 = cur
        while idx<n:
            idx += 1
            cur = cur.next
        p3 = cur
        p4 = cur.next
        # reverse p2 to p3
        tmp1, tmp2 = p2, p2.next
        while tmp1!=p3:
            tmp = tmp2.next
            tmp2.next = tmp1
            tmp1, tmp2 = tmp2, tmp
        p1.next = p3
        p2.next = p4
        return dummy.next
