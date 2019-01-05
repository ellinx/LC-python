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
class Solution:
    """
    Thoughts:
    1. BFS

    Time: O(n) where n is total number of nodes in the tree
    Space: O(n)
    """
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #BFS
        if not root:
            return[]
        ret = []
        cur = [root]
        while len(cur):
            ret.append(cur[-1].val)
            nxt = []
            for each in cur:
                if each.left:
                    nxt.append(each.left)
                if each.right:
                    nxt.append(each.right)
            cur = nxt
        return ret
