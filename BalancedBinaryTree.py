"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

"""
class Solution:
    """
    Thoughts:
    1. helper function will return if this node's all subtrees are balanced and its depth

    Time: O(n) where n is total number of nodes in the tree
    Space: O(1)
    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # check if balanced and return (isBalanced,depth)
        def helper(root):
            ret = [True, 0]
            if not root:
                return ret
            left = helper(root.left)
            right = helper(root.right)
            ret[0] = left[0] and right[0] and abs(left[1]-right[1])<2
            ret[1] = max(left[1], right[1])+1
            return ret

        return helper(root)[0]
