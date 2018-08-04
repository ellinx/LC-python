"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

"""
class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        minHeap = []
        stk = collections.deque()
        cur = root
        while cur:
            stk.append(cur)
            cur = cur.left
        while len(stk):
            cur = stk.pop()
            heapq.heappush(minHeap, [abs(target-cur.val), cur.val])
            cur = cur.right
            while cur:
                stk.append(cur)
                cur = cur.left
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(minHeap)[1])
        return ret
