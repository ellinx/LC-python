"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root is None:
                return None
            l = helper(root.left)
            r = helper(root.right)
            if l is not None and r is not None:
                root.left = None
                root.right = l[0]
                l[1].right = r[0]
                return [root, r[1]]
            if l is not None:
                root.left = None
                root.right = l[0]
                return [root, l[1]]
            if r is not None:
                return [root, r[1]]
            return [root,root]

        helper(root)
