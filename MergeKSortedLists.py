from ListNode import ListNode, listNodeList
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
class MergeKSortedLists:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        minHeap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(minHeap)
        while len(minHeap):
            temp = heapq.heappop(minHeap)
            cur.next = temp[2]
            cur = cur.next
            if temp[2].next:
                heapq.heappush(minHeap, (temp[2].next.val, temp[1], temp[2].next))
        return dummy.next
