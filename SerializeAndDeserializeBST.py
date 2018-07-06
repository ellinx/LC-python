"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should
be stateless.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *


class SerializeAndDeserializeBST:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ret = str(root.val)
        left = self.serialize(root.left)
        if left!="":
            ret += ","+left
        right = self.serialize(root.right)
        if right!="":
            ret += ","+right
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        if data=="":
            return None
        vals = data.split(",")
        ret = TreeNode(int(vals[0]))
        index = 1
        while index<len(vals):
            if int(vals[index])<int(vals[0]):
                index += 1
            else:
                break
        if index>1:
            ret.left = self.deserialize(",".join(vals[1:index]))
        if index<len(vals):
            ret.right = self.deserialize(",".join(vals[index:]))
        return ret

# Your Codec object will be instantiated and called as such:
# codec = SerializeAndDeserializeBST()
# codec.deserialize(codec.serialize(root))
