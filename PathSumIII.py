"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, sum):
            counter = dict()
            if root is None:
                return counter
            left = dfs(root.left, sum)
            right = dfs(root.right, sum)
            nonlocal total
            total += left.get(sum, 0)
            total += right.get(sum, 0)
            for k in left:
                counter[k+root.val] = counter.get(k+root.val, 0)+left[k]
            for k in right:
                counter[k+root.val] = counter.get(k+root.val, 0)+right[k]
            counter[root.val] = counter.get(root.val, 0)+1
            #print(root.val, counter)
            return counter

        total = 0
        count = dfs(root, sum)
        total += count.get(sum, 0)
        return total
