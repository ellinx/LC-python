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
class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return None
            left = helper(root.left)
            right = helper(root.right)
            ret = [0,[0,0]]
            ret[0] = root.val
            if left:
                if root.val+1==left[0]:
                    ret[1][0] = left[1][0]+1
                if root.val-1==left[0]:
                    ret[1][1] = left[1][1]+1
            if right:
                if root.val+1==right[0]:
                    ret[1][0] = max(ret[1][0], right[1][0]+1)
                if root.val-1==right[0]:
                    ret[1][1] = max(ret[1][1], right[1][1]+1)
            if ret[1][0]==0:
                ret[1][0] = 1
            if ret[1][1]==0:
                ret[1][1] = 1
            nonlocal maxPath
            maxPath = max(maxPath, ret[1][0], ret[1][1])
            if left and right:
                if root.val+1==left[0] and root.val-1==right[0]:
                    maxPath = max(maxPath, left[1][0]+1+right[1][1])
                if root.val-1==left[0] and root.val+1==right[0]:
                    maxPath = max(maxPath, left[1][1]+1+right[1][0])
            return ret

        maxPath = 0
        if not root:
            return 0
        helper(root)
        return maxPath
