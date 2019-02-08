"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        def dfs(node, curPath, curSum, target, ret):
            nxtPath = curPath+[node.val]
            nxtSum = curSum+node.val
            if node.left is None and node.right is None:
                if nxtSum==target:
                    ret.append(nxtPath)
                return
            if node.left is not None:
                dfs(node.left, nxtPath, nxtSum, target, ret)
            if node.right is not None:
                dfs(node.right, nxtPath, nxtSum, target, ret)

        if root is None:
            return []
        ret = []
        dfs(root, [], 0, sum, ret)
        return ret
