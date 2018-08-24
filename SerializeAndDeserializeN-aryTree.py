"""
Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree.
An N-ary tree is a rooted tree in which each node has no more than N children.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree







as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.



Note:

1. N is in the range of [1, 1000]
2. Do not use class member/global/static variables to store states.
    Your serialize and deserialize algorithms should be stateless.

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        def dfs(root, ret):
            if root is None:
                ret.append("#")
                return
            ret.append(str(root.val)+","+str(len(root.children)))
            for each in root.children:
                dfs(each, ret)

        ret = []
        dfs(root, ret)
        return " ".join(ret)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        def dfs(vals):
            val = next(vals).split(",")
            if val[0]=="#":
                return None
            children = [None]*int(val[1])
            for i in range(len(children)):
                children[i] = dfs(vals)
            return Node(int(val[0]), children)

        vals = iter(data.split(" "))
        return dfs(vals)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
