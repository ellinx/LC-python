"""
Given a node from a cyclic linked list which is sorted in ascending order,
write a function to insert a value into the list such that it remains a cyclic sorted list.

The given node can be a reference to any single node in the list,
and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion,
you may choose any place to insert the new value.

After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null),
you should create a new single cyclic list and return the reference to that single node.
Otherwise, you should return the original given node.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            head = Node(insertVal, None)
            head.next = head
            return head
        pre, cur = head, head.next
        if pre==cur:
            head.next = Node(insertVal,head)
            return head
        while True:
            if cur.val>=pre.val:
                if insertVal>=pre.val and insertVal<=cur.val:
                    pre.next = Node(insertVal, cur)
                    return head
            else:
                if insertVal>=pre.val or insertVal<=cur.val:
                    pre.next = Node(insertVal, cur)
                    return head
            pre, cur = cur, cur.next
            if pre==head:
                break
        head.next = Node(insertVal, head.next)
        return head
