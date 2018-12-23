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
