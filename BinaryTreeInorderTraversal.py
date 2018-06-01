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
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iteratively
        stk = collections.deque()
        ret = []
        while root:
            stk.append(root)
            root = root.left
        while len(stk):
            cur = stk.pop()
            ret.append(cur.val)
            cur = cur.right
            while cur:
                stk.append(cur)
                cur = cur.left
        return ret

#         def dfs(root, ret):
#             if not root:
#                 return
#             dfs(root.left, ret)
#             ret.append(root.val)
#             dfs(root.right, ret)

#         ret = []
#         dfs(root,ret)
#         return ret
