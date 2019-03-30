"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(root):
            head, tail = root, None
            cur = root
            while True:
                nxt = cur.right
                #print(cur.val,nxt)
                if cur.left is not None:
                    l, r = flat(cur.left)
                    #print(l.val,r.val)
                    cur.right = l
                    cur.left = None
                    r.right = nxt
                    cur = r
                if nxt is not None:
                    cur = nxt
                else:
                    tail = cur
                    break
            return [head,tail]

        if root is None:
            return
        flat(root)
