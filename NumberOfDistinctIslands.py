"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands.
An island is considered to be the same as another if and only if one island can be translated
(and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011

Given the above grid map, return 1.

Example 2:

11011
10000
00001
11011

Given the above grid map, return 3.

Notice that:

11
1

and

 1
11

are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j, cur):
            grid[i][j] = 0
            dirs = [[-1,0,"u"],[1,0,"d"],[0,-1,"l"],[0,1,"r"]]
            m, n = len(grid), len(grid[0])
            for each in dirs:
                ni, nj, di = i+each[0], j+each[1], each[2]
                if ni>=0 and ni<m and nj>=0 and nj<n and grid[ni][nj]==1:
                    cur.append(di)
                    dfs(grid, ni, nj, cur)
            cur.append("b")

        shapes = set()
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cur = []
                    dfs(grid, i, j, cur)
                    shapes.add("".join(cur))
        #print(shapes)
        return len(shapes)
