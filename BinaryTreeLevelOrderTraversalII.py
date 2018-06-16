"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        cur = [root]
        while len(cur):
            curVal = []
            nxt = []
            for each in cur:
                curVal.append(each.val)
                if each.left:
                    nxt.append(each.left)
                if each.right:
                    nxt.append(each.right)
            ret.append(curVal)
            cur = nxt
        return ret[::-1]
