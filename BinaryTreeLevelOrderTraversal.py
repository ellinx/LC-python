"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS
        ret = []
        if not root:
            return ret
        cur = [root]
        while len(cur):
            nxt = []
            vals = []
            for each in cur:
                vals.append(each.val)
                if each.left:
                    nxt.append(each.left)
                if each.right:
                    nxt.append(each.right)
            ret.append(vals)
            cur = nxt
        return ret
