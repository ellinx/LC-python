"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

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

class BinaryTreeLongestConsecutiveSequence:
    def __init__(self):
        self.ret = 0

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0
            #print(root.val)
            left = helper(root.left)
            right = helper(root.right)
            self.ret = max(self.ret, left, right)
            ret = 1
            if root.left and root.val+1==root.left.val:
                ret = max(ret, left+1)
            if root.right and root.val+1==root.right.val:
                ret = max(ret, right+1)
            return ret

        temp = helper(root)
        return max(self.ret, temp)
