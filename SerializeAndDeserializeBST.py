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
        if root is None:
            return ""

        res = str(root.val)
        if root.left is not None:
            res += "," + self.serialize(root.left)
        if root.right is not None:
            res += "," + self.serialize(root.right)

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        leftStart, rightStart = 0, 0
        if len(nodes)==1:
            return root

        for i in range(1,len(nodes)):
            if int(nodes[i]) < root.val:
                if leftStart == 0:
                    leftStart = i
            else:
                rightStart = i
                break

        if leftStart!=0:
            leftStr = ""
            if rightStart!=0:
                for i in range(leftStart,rightStart):
                    if i==leftStart:
                        leftStr = nodes[i]
                    else:
                        leftStr += ","+nodes[i]
                root.left = self.deserialize(leftStr)
            else:
                for i in range(leftStart,len(nodes)):
                    if i==leftStart:
                        leftStr = nodes[i]
                    else:
                        leftStr += ","+nodes[i]
                root.left = self.deserialize(leftStr)
        if rightStart!=0:
            rightStr = ""
            for i in range(rightStart,len(nodes)):
                if i==rightStart:
                    rightStr = nodes[i]
                else:
                    rightStr += ","+nodes[i]
            root.right = self.deserialize(rightStr)

        return root

# Your Codec object will be instantiated and called as such:
# codec = SerializeAndDeserializeBST()
# codec.deserialize(codec.serialize(root))