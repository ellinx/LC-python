"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?


"""
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root, li):
            if not root:
                return
            dfs(root.left, li)
            li.append(root)
            dfs(root.right, li)

        li = []
        dfs(root, li)
        # find the none ascending pair
        for i in range(len(li)-1):
            if li[i].val>li[i+1].val:
                break
        # find the largest value that's smaller than the li[i].val after index i and swap them
        start, end = i+1, len(li)-1
        while start<=end:
            mid = start+(end-start)//2
            if li[mid].val>li[i].val:
                end = mid-1
            else:
                start = mid+1
        li[start-1].val, li[i].val = li[i].val, li[start-1].val
