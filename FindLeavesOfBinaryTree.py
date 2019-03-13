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
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, mm):
            if root is None:
                return -1
            left = dfs(root.left, mm)
            right = dfs(root.right, mm)
            dist = max(left,right)+1
            mm[dist].append(root.val)
            return dist

        mm = collections.defaultdict(list)
        dfs(root, mm)
        return [mm[k] for k in sorted(mm)]
