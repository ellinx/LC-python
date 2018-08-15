"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, ret):
            if root is None:
                return
            dfs(root.left, ret)
            dfs(root.right, ret)
            ret.append(root.val)

        ret = []
        dfs(root,ret)
        return ret
