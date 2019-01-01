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


class Solution2:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stk = collections.deque()
        while root is not None or len(stk):
            if root is not None:
                stk.append([root,0])
                root = root.left
            else:
                root, r = stk.pop()
                if r==1:
                    ret.append(root.val)
                    root = None
                else:
                    stk.append([root, 1])
                    root = root.right
        return ret
