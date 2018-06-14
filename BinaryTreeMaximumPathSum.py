"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

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
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0
            nonlocal ret
            left = helper(root.left)
            right = helper(root.right)
            if left>0 and right>0:
                ret = max(ret, left+right+root.val)
                return max(left,right)+root.val
            if left>0:
                ret = max(ret, left+root.val)
                return left+root.val
            if right>0:
                ret = max(ret, right+root.val)
                return right+root.val
            ret = max(ret, root.val)
            return root.val

        ret = float('-inf')
        helper(root)
        return ret
