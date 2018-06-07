import TreeNode
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, start, end):
            if start>end:
                return None
            if start==end:
                return TreeNode(nums[start])
            mid = start+(end-start)//2
            ret = TreeNode(nums[mid])
            ret.left = helper(nums, start, mid-1)
            ret.right = helper(nums, mid+1, end)
            return ret

        return helper(nums, 0, len(nums)-1)
