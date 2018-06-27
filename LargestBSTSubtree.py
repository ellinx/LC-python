"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:

    10
    / \
   5  15
  / \   \
 1   8   7

The Largest BST Subtree in this case is the highlighted one.

   5
  / \
 1   8

The return value is the subtree's size, which is 3.

Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""
class Solution:
    """
    Thoughts:
    1. recursive function that takes a tree node and return [min, max, num] where min is minimum val of this subtree, max is maximum value of this subtree and num  is total number of nodes in this subtree

    Time: O(n) where n is number of nodes in the tree
    Space: O(1)
    """
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return None
            left = helper(root.left)
            right = helper(root.right)
            ret = [0]*3
            if left:
                if left[2]==0:
                    return [0]*3
                if root.val>left[1]:
                    ret[0] = left[0]
                    ret[2] += left[2]
                else:
                    ret[2] = -1
            else:
                ret[0] = root.val
            if right:
                if right[2]==0:
                    return [0]*3
                if root.val<right[0] and right[2]:
                    ret[1] = right[1]
                    ret[2] += right[2]
                else:
                    ret[2] = -1
            else:
                ret[1] = root.val
            ret[2] += 1
            nonlocal maxBST
            maxBST = max(maxBST, ret[2])
            #print(ret,root.val)
            return ret

        maxBST = 0
        helper(root)
        return maxBST
