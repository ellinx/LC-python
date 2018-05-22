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
class InorderSuccessorInBST(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # iterative way
        stk = []
        while root:
            if root.val==p.val:
                break
            if root.val>p.val:
                stk.append(root)
                root = root.left
            else:
                root = root.right
        root = root.right
        while root:
            stk.append(root)
            root = root.left
        if not len(stk):
            return None
        return stk[-1]
