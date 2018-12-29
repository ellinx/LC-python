import TreeLinkNode
"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}

Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

1. You may only use constant extra space.
2. Recursive approach is fine, implicit stack space does not count as extra space for this problem.

Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7

After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL


"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        head, pre = None, None
        node = root
        while node is not None:
            if node.left is not None:
                if head is None:
                    head, pre = node.left, node.left
                else:
                    pre.next = node.left
                    pre = pre.next
            if node.right is not None:
                if head is None:
                    head, pre = node.right, node.right
                else:
                    pre.next = node.right
                    pre = pre.next
            node = node.next
            if node is None:
                node = head
                head, pre = None, None
