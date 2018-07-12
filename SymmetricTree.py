"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively. 
"""
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(l,r):
            if l and r:
                if l.val!=r.val:
                    return False
                return helper(l.left, r.right) and helper(l.right, r.left)
            if not l and not r:
                return True
            return False

        if not root:
            return True
        return helper(root.left,root.right)
