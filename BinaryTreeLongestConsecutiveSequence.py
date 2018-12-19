from TreeNode import TreeNode

"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:
Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if root is None:
                return [[0,0],0]
            ret = [[root.val,1],0]
            l, maxl = helper(root.left)
            r, maxr = helper(root.right)
            if root.val+1==l[0]:
                ret[0][1] = max(ret[0][1], l[1]+1)
            if root.val+1==r[0]:
                ret[0][1] = max(ret[0][1], r[1]+1)
            ret[1] = max(ret[1], ret[0][1], maxl, maxr)
            return ret

        return helper(root)[1]
