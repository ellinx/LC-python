from TreeNode import TreeNode

"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

class DiameterOfBinaryTree:
    def __init__(self):
        self.diameter = 0

    # use a recursive helper function that takes a TreeNode root as input
    # update longest path with a new candidate which is longest path ends at left child, root and longest path ends at right child
    # return longest path ends at root
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path(root):
            if not root:
                return 0
            left = path(root.left)
            right = path(root.right)
            self.diameter = max(self.diameter, left+right+1)
            return max(left,right)+1

        path(root)
        return self.diameter-1 if self.diameter>0 else self.diameter
