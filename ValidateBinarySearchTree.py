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

class ValidateBinarySearchTree:
    # inorder traverse a BST, it should be in ascending order
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = float('-inf')
        stk = collections.deque()
        while root:
            stk.append(root)
            root = root.left
        while len(stk):
            root = stk.pop()
            if pre>=root.val:
                return False
            pre = root.val
            root = root.right
            while root:
                stk.append(root)
                root = root.left
        return True
