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

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # ---pos1 pos2---pre cur----
        if k==1 or not head:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        count //= k
        dummy = ListNode(0)
        dummy.next = head
        pos1 = dummy
        pos2 = head
        pre = head
        cur = head.next
        while count:
            for _ in range(k-1):
                nextCur = cur.next
                cur.next = pre
                pre, cur = cur, nextCur
            pos1.next = pre
            pos2.next = cur
            count -= 1
            if not count:
                break
            pos1, pos2 = pos2, cur
            pre, cur = cur, cur.next
        return dummy.next
