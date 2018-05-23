"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ReverseLinkedList:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursive
        def helper(root):
            #print(root.val)
            if not root.next:
                nonlocal ret
                ret = root
                return root
            helper(root.next).next = root
            root.next = None
            return root
        if not head:
            return head
        ret = None
        helper(head)
        return ret

        # iterative
        # pre = None
        # cur = head
        # while cur:
        #     nextCur = cur.next
        #     cur.next = pre
        #     pre, cur = cur, nextCur
        # return pre
