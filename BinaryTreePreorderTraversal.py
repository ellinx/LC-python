"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stk = collections.deque()
        cur = root
        while cur or len(stk):
            if cur:
                ret.append(cur.val)
                stk.append(cur)
                cur = cur.left
            else:
                cur = stk.pop()
                cur = cur.right
        return ret
