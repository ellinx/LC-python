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
            if root is None:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            #print(root.val,l,r)
            nonlocal ret
            ret = max(ret, root.val+l+r, root.val+l, root.val+r, root.val)
            return root.val+max(0, l, r)

        ret = float("-inf")
        helper(root)
        return ret
