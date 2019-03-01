"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if root is None:
            return ret
        cur = [root]
        while len(cur):
            vals, nxt = [], []
            for each in cur:
                vals.append(each.val)
                if each.left is not None:
                    nxt.append(each.left)
                if each.right is not None:
                    nxt.append(each.right)
            ret.append(vals)
            cur = nxt
        return ret[::-1]
