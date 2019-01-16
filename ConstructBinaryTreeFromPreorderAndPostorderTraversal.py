"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:
1. 1 <= pre.length == post.length <= 30
2. pre[] and post[] are both permutations of 1, 2, ..., pre.length.
3. It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre)==0:
            return None
        if len(pre)==1:
            return TreeNode(pre[0])
        #print(pre,post)
        ret = TreeNode(pre[0])
        lPreStart = 1
        rPostEnd = len(post)-2
        # only one child, set it as left child
        if pre[lPreStart]==post[rPostEnd]:
            ret.left = self.constructFromPrePost(pre[1:],post[:-1])
            return ret
        rPreStart = pre.index(post[rPostEnd])
        lPostEnd = post.index(pre[lPreStart])
        #print(lPreStart,rPreStart,lPostEnd,rPostEnd)
        ret.left = self.constructFromPrePost(pre[lPreStart:rPreStart], post[:lPostEnd+1])
        ret.right = self.constructFromPrePost(pre[rPreStart:], post[lPostEnd+1:rPostEnd+1])
        return ret
