import TreeNode
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
class SubtreeOfAnotherTree:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSameTree(t1, t2):
            if (not t1 and t2) or (t1 and not t2):
                return False
            if not t1 and not t2:
                return True
            if t1.val!=t2.val:
                return False
            return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        if isSameTree(s,t):
            return True
        if s and (self.isSubtree(s.left,t) or self.isSubtree(s.right,t)):
            return True
        return False
