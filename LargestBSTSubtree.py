"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
where largest means subtree with largest number of nodes in it.

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
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def getInfo(root):
            nonlocal ret
            if root is None:
                return None
            if root.left is None and root.right is None:
                ret = max(ret, 1)
                #print(root.val, ret)
                return [root.val, root.val, root.val, 1]
            if root.left is None:
                r = getInfo(root.right)
                if r is not None and root.val < r[0]:
                    ret = max(ret, r[3]+1)
                    #print(root.val, ret)
                    return [root.val, root.val, r[2], r[3]+1]
                return None
            if root.right is None:
                l = getInfo(root.left)
                if l is not None and root.val > l[2]:
                    ret = max(ret, l[3]+1)
                    #print(root.val, ret)
                    return [l[0], root.val, root.val, l[3]+1]
                return None
            l, r = getInfo(root.left), getInfo(root.right)
            if l is None or r is None:
                return None
            if l[2]<root.val and root.val<r[0]:
                ret = max(ret, l[3]+r[3]+1)
                #print(root.val, ret)
                return [l[0], root.val, r[2], l[3]+r[3]+1]
            return None

        ret = 0
        getInfo(root)
        return ret
