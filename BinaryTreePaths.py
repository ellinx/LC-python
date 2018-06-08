"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


"""
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if not root:
            return ret
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if len(left)==0 and len(right)==0:
            ret.append(str(root.val))
            return ret
        if len(left):
            for each in left:
                ret.append(str(root.val)+"->"+each)
        if len(right):
            for each in right:
                ret.append(str(root.val)+"->"+each)
        return ret
