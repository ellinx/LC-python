from ListNode import ListNode, listNodeList

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                cur.next = l1
                cur, l1 = cur.next, l1.next
            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2
        return dummy.next

if __name__=="__main__":
    l1 = listNodeList([1,2,4])
    l2 = listNodeList([1,3,4])
    tmp = MergeTwoSortedLists()
    result = tmp.mergeTwoLists(l1, l2)
    print(result)
