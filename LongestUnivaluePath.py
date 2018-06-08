"""
Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5

Output:

2

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

Output:

2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return (val, length of path)
        def helper(root):
            if not root:
                return (None, 0)
            left = helper(root.left)
            right = helper(root.right)
            nonlocal ret
            if left[0]==root.val and right[0]==root.val:
                ret = max(ret, left[1]+1+right[1])
                return (root.val, max(left[1],right[1])+1)
            if left[0]==root.val:
                ret = max(ret, left[1]+1)
                return (root.val, left[1]+1)
            if right[0]==root.val:
                ret = max(ret, right[1]+1)
                return (root.val, right[1]+1)
            ret = max(ret, 1)
            return (root.val, 1)

        ret = 0
        helper(root)
        if ret==0:
            return ret
        return ret-1
