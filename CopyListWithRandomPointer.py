"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    #1 first loop: copy list without random pointer, memorize copied node
    #2 second loop: assign correct random pointer for each copied node
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0, None, None)
        mm = dict()
        n1, n2 = head, dummy
        while n1 is not None:
            tmp = Node(n1.val, None, None)
            mm[n1] = tmp
            n2.next = tmp
            n1, n2 = n1.next, n2.next
        n1, n2 = head, dummy.next
        while n1 is not None:
            if n1.random is not None:
                n2.random = mm[n1.random]
            n1, n2 = n1.next, n2.next
        return dummy.next


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution2(object):
    # without map
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # copy original node and combine origianl and copied node in one list
        # then seperate them
        if not head:
            return None
        # copy nodes
        cur = head
        while cur:
            copied = RandomListNode(cur.label)
            copied.next = cur.next
            cur.next = copied
            cur = copied.next
        # set random pointer
        cur = head
        copied = cur.next
        while cur:
            if cur.random:
                copied.random = cur.random.next
            cur = copied.next
            if cur:
                copied = cur.next
        # seperate original with copied
        dummy = RandomListNode(0)
        cur = head
        copied = dummy
        while cur:
            copied.next = cur.next
            copied = copied.next
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
