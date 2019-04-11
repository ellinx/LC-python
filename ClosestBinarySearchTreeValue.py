"""
Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Note:
1. Given target value is a floating point.
2. You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ret = root.val
        while root is not None:
            if abs(ret-target)>abs(root.val-target):
                ret = root.val
            if root.val>target:
                root = root.left
            else:
                root = root.right
        return ret
