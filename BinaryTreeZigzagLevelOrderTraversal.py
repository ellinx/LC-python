"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

"""
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        cur = [root]
        lToR = True
        ret = []
        while len(cur):
            vals = []
            nxt = []
            for each in cur:
                vals.append(each.val)
                if each.left:
                    nxt.append(each.left)
                if each.right:
                    nxt.append(each.right)
            if lToR:
                lToR = False
                ret.append(vals)
            else:
                lToR = True
                ret.append(vals[::-1])
            cur = nxt
        return ret
