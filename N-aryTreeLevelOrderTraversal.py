"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:




We should return its level order traversal:





[
     [1],
     [3,2,4],
     [5,6]
]



Note:

    The depth of the tree is at most 1000.
    The total number of nodes is at most 5000.

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ret = []
        if root is None:
            return ret
        cur = [root]
        while len(cur):
            nxt = []
            vals = []
            for each in cur:
                vals.append(each.val)
                for child in each.children:
                    if child:
                        nxt.append(child)
            ret.append(vals)
            cur = nxt
        return ret
