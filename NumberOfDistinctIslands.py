"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands.
An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

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
        def dfs(grid, i, j):
            grid[i][j] = 0
            ret = ""
            # up
            if i-1>=0 and grid[i-1][j]==1:
                ret += 'u'+dfs(grid, i-1, j)
            # down
            if i+1<len(grid) and grid[i+1][j]==1:
                ret += 'd'+dfs(grid, i+1, j)
            # left
            if j-1>=0 and grid[i][j-1]==1:
                ret += 'l'+dfs(grid, i, j-1)
            # right
            if j+1<len(grid[0]) and grid[i][j+1]==1:
                ret += 'r'+dfs(grid, i, j+1)
            ret += 'e'
            return ret

        shape = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    shape.add(dfs(grid, i, j))
        #print(shape)
        return len(shape)

class Solution2:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j, r0, c0, cur):
            m, n = len(grid), len(grid[0])
            if grid[i][j]!=1:
                return
            grid[i][j] = 0
            cur.add((i-r0)*2*n+(j-c0))
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            for each in dirs:
                ni = i+each[0]
                nj = j+each[1]
                if ni>=0 and ni<m and nj>=0 and nj<n:
                    dfs(grid, ni, nj, r0, c0, cur)

        # record point from top left
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        shapes = set()
        for i in range(m):
            for j in range(n):
                cur = set()
                dfs(grid, i, j, i, j, cur)
                if len(cur)!=0:
                    shapes.add(tuple(sorted(cur)))
        return len(shapes)
