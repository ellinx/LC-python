"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree

          1
         / \
        2   3
       / \
      4   5

Returns [4, 5, 3], [2], [1].

Explanation:

1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2

2. Now removing the leaf [2] would result in this tree:

          1

3. Now removing the leaf [1] would result in the empty tree:

          []

Returns [4, 5, 3], [2], [1]. 
"""
class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(root, lengthToLeave):
            if not root:
                return -1
            left = helper(root.left, lengthToLeave)
            right = helper(root.right, lengthToLeave)
            if left==-1 and right==-1:
                lengthToLeave[0].append(root.val)
                return 0
            if left==-1:
                lengthToLeave[right+1].append(root.val)
                return right+1
            if right==-1:
                lengthToLeave[left+1].append(root.val)
                return left+1
            temp = max(left,right)
            lengthToLeave[temp+1].append(root.val)
            return temp+1

        if not root:
            return []
        lengthToLeave = collections.defaultdict(list)
        helper(root, lengthToLeave)
        ret = [[]]*(max(lengthToLeave.keys())+1)
        for k in lengthToLeave:
            ret[k] = lengthToLeave[k]
        return ret
