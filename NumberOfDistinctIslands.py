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
        # record the dfs path of each island
        def dfs(grid, row, col, cur, path):
            grid[row][col] = 0
            path.append(cur)
            # up
            if row and grid[row-1][col]==1:
                dfs(grid, row-1, col, "u" ,path)
            # down
            if row<len(grid)-1 and grid[row+1][col]==1:
                dfs(grid, row+1, col, "d", path)
            # left
            if col and grid[row][col-1]==1:
                dfs(grid, row, col-1, "l", path)
            # right
            if col<len(grid[0])-1 and grid[row][col+1]==1:
                dfs(grid, row, col+1, "r", path)
            path.append("e")

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    path = []
                    dfs(grid, i, j, "s", path)
                    #print(path)
                    islands.add("".join(path))
        #print(islands)
        return len(islands)
