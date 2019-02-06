"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node
to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxSumFromRoot(root):
            if root is None:
                return float('-inf')
            left = maxSumFromRoot(root.left)
            right = maxSumFromRoot(root.right)
            nonlocal ret
            ret = max(ret, left+root.val, right+root.val, left+right+root.val, root.val)
            return max(left+root.val, right+root.val, root.val)

        ret = float('-inf')
        maxSumFromRoot(root)
        return ret
