"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.
"""
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        cur = []
        cur.append(root)
        while len(cur):
            total = 0
            nxt = []
            for node in cur:
                total += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            ret.append(total/len(cur))
            cur = nxt
        return ret
