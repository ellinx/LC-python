"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

   a1-a2--
          |-c1-c2-c3
b1-b2-b3--

begin to intersect at node c1.


Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
    There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4].
    There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
    Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:
1. If the two linked lists have no intersection at all, return null.
2. The linked lists must retain their original structure after the function returns.
3. You may assume there are no cycles anywhere in the entire linked structure.
4. Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        if headA==headB:
            return headA
        cur1, cnt1 = headA, 1
        while cur1.next is not None:
            cnt1 += 1
            cur1 = cur1.next
        cur2, cnt2 = headB, 1
        while cur2.next is not None:
            cnt2 += 1
            cur2 = cur2.next
        if cur1!=cur2:
            return None
        if cnt1<=cnt2:
            cur1, cur2 = headA, headB
            for _ in range(cnt2-cnt1):
                cur2 = cur2.next
        else:
            cur1, cur2 = headA, headB
            for _ in range(cnt1-cnt2):
                cur1 = cur1.next
        while cur1!=cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        if headA==headB:
            return headA
        cur1, cur2 = headA, headB
        while cur1!=cur2:
            if cur1 is not None:
                cur1 = cur1.next
            else:
                cur1 = headB
            if cur2 is not None:
                cur2 = cur2.next
            else:
                cur2 = headA
        return cur1
