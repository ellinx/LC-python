"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:




We should return its level order traversal:

         1
       / |  \
     3   2   4
    /  \
   5    6

[
     [1],
     [3,2,4],
     [5,6]
]



Note:
1. The depth of the tree is at most 1000.
2. The total number of nodes is at most 5000.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if root is None:
            return []
        ret = []
        cur = [root]
        while len(cur)>0:
            vals = []
            nxt = []
            for each in cur:
                vals.append(each.val)
                for child in each.children:
                    nxt.append(child)
            ret.append(vals)
            cur = nxt
        return ret
