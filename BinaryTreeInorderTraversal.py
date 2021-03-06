import collections
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    recursive
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def visit(root,ret):
            if root is None:
                return
            visit(root.left, ret)
            ret.append(root.val)
            visit(root.right, ret)

        ret = []
        visit(root, ret)
        return ret

class Solution2:
    """
    use stack
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stk = collections.deque()
        while root is not None or len(stk):
            if root is not None:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                ret.append(root.val)
                root = root.right
        return ret

class Solution3:
    """
    Morris traversal
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        cur = root
        while cur is not None:
            if cur.left is None:
                ret.append(cur.val)
                cur = cur.right
                continue
            pre = cur.left
            while pre.right is not None and pre.right!=cur:
                pre = pre.right
            if pre.right==cur:
                pre.right = None
                ret.append(cur.val)
                cur = cur.right
            else:
                pre.right = cur
                cur = cur.left
        return ret
