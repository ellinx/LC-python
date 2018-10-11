"""

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l, cur = 1, root.left
        while cur is not None:
            l += 1
            cur = cur.left
        r, cur = 1, root.right
        while cur is not None:
            r += 1
            cur = cur.right
        if l==r:
            return 2**l-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


class Solution2:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        cur = [root]
        ret = 0
        while len(cur):
            ret += len(cur)
            nxt = []
            for each in cur:
                if each.left is not None:
                    nxt.append(each.left)
                else:
                    break
                if each.right is not None:
                    nxt.append(each.right)
                else:
                    break
            cur = nxt
        return ret
