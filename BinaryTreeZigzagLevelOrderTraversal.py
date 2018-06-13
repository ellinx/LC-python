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
        if not root:
            return []
        # order 0 left->right, 1 right->left
        order = 0
        cur = [root]
        ret = []
        while len(cur):
            nxt = []
            if order==0:
                ret.append([cur[i].val for i in range(len(cur))])
            else:
                ret.append([cur[i].val for i in range(len(cur)-1,-1,-1)])
            for each in cur:
                if each.left:
                    nxt.append(each.left)
                if each.right:
                    nxt.append(each.right)
            order = 1-order
            cur = nxt
        return ret
