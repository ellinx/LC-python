"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class CopyListWithRandomPointer(object):
    #1 first loop: copy list without random pointer, memorize copied node
    #2 second loop: assign correct random pointer for each copied node
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        copy = {}
        dummy1, dummy2 = RandomListNode(0), RandomListNode(0)
        dummy1.next = head
        cur = head
        copyPre = dummy2
        #copy next
        while cur:
            copy[cur.label] = RandomListNode(cur.label)
            copyPre.next = copy[cur.label]
            copyPre, cur = copyPre.next, cur.next
        cur = head
        copyCur = dummy2.next
        #copy random
        while cur:
            if cur.random:
                copyCur.random = copy[cur.random.label]
            copyCur, cur = copyCur.next, cur.next
        return dummy2.next
