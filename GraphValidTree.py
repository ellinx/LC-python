"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def findRoot(roots, node):
            while roots[node]!=node:
                node = roots[node]
            return node

        roots = [i for i in range(n)]
        total = n
        for edge in edges:
            root0 = findRoot(roots, edge[0])
            root1 = findRoot(roots, edge[1])
            roots[edge[0]] = root0
            roots[edge[1]] = root1
            if root0==root1:
                return False
            roots[root1] = root0
            total -= 1
        return total==1

class Solution2:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges)!=n-1:
            return False
        g = collections.defaultdict(set)
        for edge in edges:
            g[edge[0]].add(edge[1])
            g[edge[1]].add(edge[0])
        visited = [False]*n
        q = collections.deque()
        q.append(0)
        visited[0] = True
        while len(q):
            cur = q.popleft()
            for neighbors in g[cur]:
                if not visited[neighbors]:
                    visited[neighbors] = True
                    g[neighbors].remove(cur)
                    q.append(neighbors)
            g.pop(cur)
        for each in visited:
            if not each:
                return False
        return len(g)==0
