"""
You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.

These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(0, None, None, None)
        stk = collections.deque()
        cur1, cur2 = dummy, head
        while cur2 is not None or len(stk)>0:
            if cur2 is not None:
                cur1.next, cur2.prev = cur2, cur1
                cur1.child = None
                if cur2.child is not None:
                    stk.append(cur2.next)
                    cur1, cur2 = cur1.next, cur2.child
                    continue
                cur1, cur2 = cur1.next, cur2.next
            else:
                cur2 = stk.pop()
        ret = dummy.next
        if ret is not None:
            ret.prev = None
        return ret
