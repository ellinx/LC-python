"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""


class RemoveLinkedListElements:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newHead = None
        if head == None:
            return newHead

        pre = None
        cur = head
        while cur != None:
            if newHead == None:
                if cur.val == val:
                    pre = cur
                    cur = cur.next
                else:
                    newHead = cur
                    pre = cur
                    cur = cur.next
            else:
                if cur.val == val:
                    pre.next = cur.next
                    cur = cur.next
                else:
                    pre = cur
                    cur = cur.next

        return newHead


# test
from ListNode import *
if __name__=="__main__":
    test = RemoveLinkedListElements()
    head = initList([1,2,6,3,4,5,6])
    result = test.removeElements(head, 6)
    printList(result)