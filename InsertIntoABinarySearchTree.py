"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""
import TreeNode

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        stk = collections.deque()
        pre = None
        cur = root
        while cur is not None or len(stk):
            if cur is not None:
                stk.append(cur)
                cur = cur.left
            else:
                cur = stk.pop()
                if cur.val>val:
                    break
                pre = cur
                cur = cur.right
        if cur is None:
            pre.right = TreeNode(val)
            return root
        #print(cur.val)
        if cur.left is None:
            cur.left = TreeNode(val)
            return root
        cur = cur.left
        while cur.right is not None:
            cur = cur.right
        cur.right = TreeNode(val)
        return root
