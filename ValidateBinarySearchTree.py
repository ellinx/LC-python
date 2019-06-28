from TreeNode import TreeNode

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
is 5 but its right child's value is 4.
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stk = collections.deque()
        pre = None
        while root is not None or len(stk)>0:
            if root is not None:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                if pre is not None and pre.val>=root.val:
                    return False
                pre = root
                root = root.right
        return True


class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, lbound, rbound):
            if root is None:
                return True
            if root.val<=lbound or root.val>=rbound:
                return False
            return dfs(root.left, lbound, root.val) and dfs(root.right, root.val, rbound)

        return dfs(root, float('-inf'), float('inf'))
