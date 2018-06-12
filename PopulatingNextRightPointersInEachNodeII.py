import TreeLinkNode
"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    Recursive approach is fine, implicit stack space does not count as extra space for this problem.

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
        pre, cur, start = None, root, None
        while cur:
            while cur:
                if cur.left:
                    if not start:
                        start = cur.left
                    if pre:
                        pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    if not start:
                        start = cur.right
                    if pre:
                        pre.next = cur.right
                    pre = cur.right
                cur = cur.next
            pre, cur, start = None, start, None
