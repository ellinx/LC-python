"""
Given a binary tree, collect a tree's nodes as if you were doing this:
Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree

          1
         / \
        2   3
       / \
      4   5

Returns [4, 5, 3], [2], [1].

Explanation:

1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2

2. Now removing the leaf [2] would result in this tree:

          1

3. Now removing the leaf [1] would result in the empty tree:

          []

Returns [4, 5, 3], [2], [1].
"""
class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(root, mm):
            if root is None:
                return 0
            if root in mm:
                return mm[root]
            mm[root] = max(helper(root.left, mm), helper(root.right, mm))+1
            return mm[root]

        mm = dict()
        height = helper(root, mm)
        ret = [[] for _ in range(height)]
        for k in mm:
            ret[mm[k]-1].append(k.val)
        return ret
