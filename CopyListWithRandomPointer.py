"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    #1 first loop: copy list without random pointer, memorize copied node
    #2 second loop: assign correct random pointer for each copied node
    def copyRandomList(self, head: 'Node') -> 'Node':
        mm = dict()
        dummy = Node(0,None,None)
        cur, cur1 = head, dummy
        while cur is not None:
            mm[cur] = Node(cur.val, None, None)
            cur1.next = mm[cur]
            cur, cur1 = cur.next, cur1.next
        cur, cur1 = head, dummy.next
        while cur is not None:
            if cur.random is not None:
                cur1.random = mm[cur.random]
            cur, cur1 = cur.next, cur1.next
        return dummy.next

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
