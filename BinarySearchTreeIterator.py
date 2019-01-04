from TreeNode import TreeNode
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""

class BSTIterator(object):
    # use iterative way of inorder traverse a BST
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = collections.deque()
        while root:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk)>0

    def next(self):
        """
        :rtype: int
        """
        ret = self.stk.pop()
        cur = ret.right
        while cur:
            self.stk.append(cur)
            cur = cur.left
        return ret.val

class BSTIterator2:
    """
    Morris traverse
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.pre, self.cur = None, root
        self.hasNextCalled = False

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.hasNextCalled:
            self.hasNext()
        ret = self.cur.val
        self.cur = self.cur.right
        return ret

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        while self.cur is not None:
            if self.cur.left is None:
                break
            self.pre = self.cur.left
            while self.pre.right is not None and self.pre.right!=self.cur:
                self.pre = self.pre.right
            if self.pre.right is None:
                self.pre.right = self.cur
                self.cur = self.cur.left
            else:
                self.pre.right = None
                break
        self.hasNextCalled = True
        return self.cur is not None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
