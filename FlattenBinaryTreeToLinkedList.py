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
        def flatTree(root):
            if root is None:
                return [None, None]
            lhead, ltail = flatTree(root.left)
            rhead, rtail = flatTree(root.right)
            root.left = None
            ret = [root, root]
            if lhead is not None:
                ret[1].right = lhead
                ret[1] = ltail
            if rhead is not None:
                ret[1].right = rhead
                ret[1] = rtail
            return ret

        flatTree(root)
