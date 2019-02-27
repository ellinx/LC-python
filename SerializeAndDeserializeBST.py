"""
Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states.
        Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        stk = collections.deque()
        while root is not None or len(stk)>0:
            if root is not None:
                ret.append(str(root.val))
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                root = root.right
        return " ".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def insert(root, val):
            pre = None
            while root is not None:
                pre = root
                if root.val<val:
                    root = root.right
                else:
                    root = root.left
            if pre.val>val:
                pre.left = TreeNode(val)
            else:
                pre.right = TreeNode(val)

        if len(data)==0:
            return None
        data = data.split(" ")
        ret = TreeNode(int(data[0]))
        for i in range(1,len(data)):
            insert(ret, int(data[i]))
        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
