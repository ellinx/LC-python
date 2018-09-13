"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        stk = collections.deque()
        cur = head
        length = (length+1)//2
        while length:
            length -= 1
            cur = cur.next
        while cur:
            stk.append(cur)
            cur = cur.next
        dummy = ListNode(0)
        cur1 = dummy
        cur = head
        while len(stk):
            cur1.next = cur
            cur = cur.next
            cur1 = cur1.next

            cur1.next = stk.pop()
            cur1 = cur1.next
        if cur:
            cur1.next = cur
            cur1 = cur1.next
        cur1.next = None
