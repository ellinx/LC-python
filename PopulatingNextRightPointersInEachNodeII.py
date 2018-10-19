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
                if cur.left is not None:
                    if head is None:
                        head = cur.left
                        pre = cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right is not None:
                    if head is None:
                        head = cur.right
                        pre = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
            cur = head
            head, pre = None, None
