"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing.
For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

Note: All the values of tree nodes are in the range of [-1e7, 1e7].

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, ret):
            if root is None:
                return [[0,0], [0,0]]
            li, ld = helper(root.left, ret)
            ri, rd = helper(root.right, ret)
            rooti, rootd = [root.val, 1], [root.val, 1]
            if li[0]+1==root.val:
                rooti[1] = li[1]+1
                if root.val+1==rd[0]:
                    ret[0] = max(ret[0], li[1]+1+rd[1])
                else:
                    ret[0] = max(ret[0], li[1]+1)
            if ld[0]-1==root.val:
                rootd[1] = ld[1]+1
                if root.val-1==ri[0]:
                    ret[0] = max(ret[0], ld[1]+1+ri[1])
                else:
                    ret[0] = max(ret[0], ld[1]+1)
            if root.val+1==rd[0]:
                rootd[1] = max(rootd[1], rd[1]+1)
                ret[0] = max(ret[0], 1+rd[1])
            if root.val-1==ri[0]:
                rooti[1] = max(rooti[1], ri[1]+1)
                ret[0] = max(ret[0], 1+ri[1])
            return [rooti, rootd]

        if root is None:
            return 0
        ret = [1]
        helper(root, ret)
        return ret[0]
