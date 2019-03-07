"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Thoughts:
    1. BFS

    Time: O(n) where n is total number of nodes in the tree
    Space: O(n)
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ret = []
        cur = [root]
        while len(cur)>0:
            nxt = []
            ret.append(cur[-1].val)
            for each in cur:
                if each.left is not None:
                    nxt.append(each.left)
                if each.right is not None:
                    nxt.append(each.right)
            cur = nxt
        return ret
