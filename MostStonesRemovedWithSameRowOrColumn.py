"""
On a 2D plane, we place stones at some integer coordinate points.
Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?


Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:
Input: stones = [[0,0]]
Output: 0


Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        def findRoot(roots, node):
            if node not in roots:
                roots[node] = node
                return node
            while roots[node]!=node:
                node = roots[node]
            return node

        connected = 0
        roots = dict()
        for i,j in stones:
            if (i,-1) not in roots:
                connected += 1
            rooti = findRoot(roots, (i,-1))
            if (-1,j) not in roots:
                connected += 1
            rootj = findRoot(roots, (-1,j))
            if rooti!=rootj:
                connected -= 1
                roots[rooti] = rootj
        return len(stones)-connected
