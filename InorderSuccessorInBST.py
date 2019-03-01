"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:
Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

Output: null
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        pre = None
        stk = collections.deque()
        while root is not None or len(stk)>0:
            if root is not None:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                if pre==p:
                    return root
                pre = root
                root = root.right
        return None
