"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4


"""
class Solution:
    """
    Thoughts:
    1. similar like search a target in BST

    Time: O(n) where n is total number of nodes in the tree
    Space: O(1)
    """
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ret = None
        while root:
            if ret==None or abs(root.val-target)<abs(ret-target):
                ret = root.val
            if root.val==target:
                break
            if root.val>target:
                root = root.left
            else:
                root = root.right
        return ret
