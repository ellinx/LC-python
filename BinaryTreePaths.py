"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, cur, ret):
            if node.left is None and node.right is None:
                ret.append(cur)
                return
            if node.left is not None:
                dfs(node.left, cur+"->"+str(node.left.val), ret)
            if node.right is not None:
                dfs(node.right, cur+"->"+str(node.right.val), ret)

        ret = []
        if root is None:
            return []
        dfs(root, str(root.val), ret)
        return ret
