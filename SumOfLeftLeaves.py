import TreeNode
"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively.
Return 24.
"""
class SumOfLeftLeaves:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        if not root:
            return ret
        if root.left and root.left.left==None and root.left.right==None:
            ret += root.left.val
        else:
            ret += self.sumOfLeftLeaves(root.left)
        ret += self.sumOfLeftLeaves(root.right)
        return ret
