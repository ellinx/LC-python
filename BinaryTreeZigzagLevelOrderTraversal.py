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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        flag = 0
        ret = []
        cur = [root]
        while len(cur)>0:
            vals = []
            nxt = []
            for each in cur:
                vals.append(each.val)
                if each.left is not None:
                    nxt.append(each.left)
                if each.right is not None:
                    nxt.append(each.right)
            if flag==0:
                ret.append(vals)
            else:
                ret.append(vals[::-1])
            flag = 1-flag
            cur = nxt
        return ret
