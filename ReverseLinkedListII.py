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
        # ----pos1 pos2----pre cur-----
        if m==n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pos1 = dummy
        count = 1
        while count<m:
            pos1 = pos1.next
            count += 1
        pos2 = pos1.next
        pre = pos2
        cur = pre.next
        for _ in range(n-m):
            nextCur = cur.next
            cur.next = pre
            pre, cur = cur, nextCur
        pos1.next = pre
        pos2.next = cur
        return dummy.next
