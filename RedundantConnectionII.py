"""
In this problem, a rooted tree is a directed graph such that,
there is exactly one node (the root) for which all other nodes are descendants of this node,
plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes
(with distinct values 1, 2, ..., N), with one additional directed edge added.
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges.
Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v,
where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

Note:
1. The size of the input 2D-array will be between 3 and 1000.
2. Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""
class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        parent = [i for i in range(N+1)]
        can = []
        for edge in edges:
            if parent[edge[1]]==edge[1]:
                parent[edge[1]] = edge[0]
            else:
                can = [[parent[edge[1]],edge[1]],edge]
                break
        #union&find
        parent = [i for i in range(N+1)]
        for edge in edges:
            if len(can)!=0 and edge==can[1]:
                continue
            r0 = parent[edge[0]]
            while parent[r0]!=r0:
                r0 = parent[r0]
            if r0!= edge[1] and parent[edge[1]]==edge[1]:
                parent[edge[1]] = edge[0]
            else:
                if len(can)==0:
                    return edge
                return can[0]
        return can[1]
