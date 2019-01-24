"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:
1. A solution using O(n) space is pretty straight forward.
2. Could you devise a constant space solution?


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root, swap):
            if root is None:
                return
            dfs(root.left, swap)
            nonlocal pre
            if pre is not None and pre.val>root.val:
                if swap[0] is None:
                    swap[0] = pre
                    swap[1] = root
                else:
                    swap[1] = root
                    return
            pre = root
            dfs(root.right, swap)

        swap = [None]*2
        pre = None
        dfs(root, swap)
        swap[0].val, swap[1].val = swap[1].val, swap[0].val
