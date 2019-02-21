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
3. You may assume that it is a perfect binary tree (ie, all leaves are at the same level,
    and every parent has two children).

Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL


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
            return root
        cur = root
        head, pre = None, None
        while cur is not None:
            while cur is not None:
                if head is None:
                    head = cur.left
                    pre = cur.left
                else:
                    pre.next = cur.left
                    pre = pre.next
                if pre is not None:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = head
            head, pre = None, None


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
