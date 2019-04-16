"""

Given a Binary Search Tree and a target number,
return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True

Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
"""
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        numSet = set()
        stk = collections.deque()
        while root is not None or len(stk):
            if root is not None:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                if k-root.val in numSet:
                    return True
                numSet.add(root.val)
                root = root.right
        return False


class Solution2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def getNextGreater(stk):
            ret, cur = None, None
            while cur is not None or len(stk)>0:
                if cur is not None:
                    stk.append(cur)
                    cur = cur.left
                else:
                    if ret is not None:
                        break
                    cur = stk.pop()
                    ret = cur.val
                    cur = cur.right
            return [ret, stk]

        def getNextSmaller(stk):
            ret, cur = None, None
            while cur is not None or len(stk)>0:
                if cur is not None:
                    stk.append(cur)
                    cur = cur.right
                else:
                    if ret is not None:
                        break
                    cur = stk.pop()
                    ret = cur.val
                    cur = cur.left
            return [ret, stk]

        stk1 = collections.deque()
        cur = root
        while cur is not None:
            stk1.append(cur)
            cur = cur.left
        stk2 = collections.deque()
        cur = root
        while cur is not None:
            stk2.append(cur)
            cur = cur.right
        l, stk1 = getNextGreater(stk1)
        r, stk2 = getNextSmaller(stk2)
        while l<r:
            if l+r==k:
                return True
            if l+r<k:
                l, stk1 = getNextGreater(stk1)
            else:
                r, stk2 = getNextSmaller(stk2)
        return False
