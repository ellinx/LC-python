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

class Solution2:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def getPredecessor(stk):
            cur = stk.pop()
            ret = cur.val
            cur = cur.left
            while cur:
                stk.append(cur)
                cur = cur.right
            return ret

        def getSuccessor(stk):
            cur = stk.pop()
            ret = cur.val
            cur = cur.right
            while cur:
                stk.append(cur)
                cur = cur.left
            return ret

        stk1 = collections.deque()
        cur = root
        while cur:
            if cur.val==target:
                stk1.append(cur)
                break
            if cur.val<target:
                stk1.append(cur)
                cur = cur.right
            else:
                cur = cur.left
        stk2 = collections.deque()
        cur = root
        while cur:
            if cur.val==target:
                stk2.append(cur)
                break
            if cur.val<target:
                cur = cur.right
            else:
                stk2.append(cur)
                cur = cur.left
        ret = []
        val1, val2 = None, None
        for i in range(k):
            if val1 is None and len(stk1):
                val1 = getPredecessor(stk1)
            if val2 is None and len(stk2):
                val2 = getSuccessor(stk2)
            #print(val1,val2)
            if val1 is not None and val2 is not None:
                if val1==val2:
                    ret.append(val1)
                    val1, val2 = None, None
                    continue
                if target-val1<val2-target:
                    ret.append(val1)
                    val1 = None
                else:
                    ret.append(val2)
                    val2 = None
            elif val1 is not None:
                ret.append(val1)
                val1 = None
            elif val2 is not None:
                ret.append(val2)
                val2 = None
        return ret
