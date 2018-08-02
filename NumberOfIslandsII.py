"""
A 2d grid map of m rows and n columns is initially filled with water.
We may perform an addLand operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]

Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0

Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

"""
class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def findRoot(roots, m, n, i, j):
            node = i*n+j
            while roots[node]!=node:
                node = roots[node]
            return node

        ret, num = [], 0
        roots = dict()
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        for pos in positions:
            cur = pos[0]*n+pos[1]
            roots[cur] = cur
            num += 1
            for each in dirs:
                i, j = pos[0]+each[0], pos[1]+each[1]
                if i>=0 and i<m and j>=0 and j<n and i*n+j in roots:
                    root = findRoot(roots, m, n, i, j)
                    if root!=cur:
                        roots[root] = cur
                        num -= 1
                    roots[i*n+j] = roots[root]
            ret.append(num)
        return ret
